from fastapi import FastAPI, Query, Response
from pydantic import BaseModel, Field
from math import ceil

app = FastAPI()

# -----------------------------------
# DATA
# -----------------------------------

books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Smith",
        "genre": "Tech",
        "is_available": True
    },
    {
        "id": 2,
        "title": "AI Revolution",
        "author": "Andrew Ng",
        "genre": "Science",
        "is_available": True
    },
    {
        "id": 3,
        "title": "History of India",
        "author": "Ram Krishna",
        "genre": "History",
        "is_available": False
    },
    {
        "id": 4,
        "title": "Machine Learning",
        "author": "Tom Mitchell",
        "genre": "Tech",
        "is_available": True
    },
    {
        "id": 5,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Fiction",
        "is_available": True
    },
    {
        "id": 6,
        "title": "Data Science Handbook",
        "author": "Jake VanderPlas",
        "genre": "Tech",
        "is_available": False
    }
]

borrow_records = []
queue = []

record_counter = 1

# -----------------------------------
# HELPERS
# -----------------------------------

def find_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def calculate_due_date(days):
    return f"Return by Day {10 + days}"


def filter_books_logic(genre=None, author=None, is_available=None):
    filtered = books

    if genre is not None:
        filtered = [
            book for book in filtered
            if book["genre"].lower() == genre.lower()
        ]

    if author is not None:
        filtered = [
            book for book in filtered
            if author.lower() in book["author"].lower()
        ]

    if is_available is not None:
        filtered = [
            book for book in filtered
            if book["is_available"] == is_available
        ]

    return filtered


# -----------------------------------
# PYDANTIC MODELS
# -----------------------------------

class BorrowRequest(BaseModel):
    member_name: str = Field(..., min_length=2)
    book_id: int = Field(..., gt=0)
    borrow_days: int = Field(..., gt=0, le=30)
    member_id: str = Field(..., min_length=4)
    member_type: str = "regular"


class NewBook(BaseModel):
    title: str = Field(..., min_length=2)
    author: str = Field(..., min_length=2)
    genre: str = Field(..., min_length=2)
    is_available: bool = True


# -----------------------------------
# DAY 1
# -----------------------------------

@app.get("/")
def home():
    return {"message": "Welcome to City Public Library"}


@app.get("/books")
def get_books():
    available_count = len(
        [book for book in books if book["is_available"]]
    )

    return {
        "total": len(books),
        "available_count": available_count,
        "books": books
    }


@app.get("/books/summary")
def books_summary():
    genre_count = {}

    for book in books:
        genre = book["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1

    available = len([b for b in books if b["is_available"]])

    return {
        "total_books": len(books),
        "available_books": available,
        "borrowed_books": len(books) - available,
        "genre_breakdown": genre_count
    }


@app.get("/books/{book_id}")
def get_book(book_id: int):
    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    return book


@app.get("/borrow-records")
def get_records():
    return {
        "total": len(borrow_records),
        "records": borrow_records
    }

# -----------------------------------
# DAY 2 + 3
# -----------------------------------

@app.post("/borrow")
def borrow_book(data: BorrowRequest):

    global record_counter

    book = find_book(data.book_id)

    if not book:
        return {"error": "Book not found"}

    if not book["is_available"]:
        return {"error": "Book already borrowed"}

    if data.member_type == "premium":
        due_date = calculate_due_date(min(data.borrow_days, 60))
    else:
        due_date = calculate_due_date(min(data.borrow_days, 30))

    book["is_available"] = False

    record = {
        "record_id": record_counter,
        "member_name": data.member_name,
        "member_id": data.member_id,
        "book_title": book["title"],
        "borrow_days": data.borrow_days,
        "due_date": due_date
    }

    borrow_records.append(record)

    record_counter += 1

    return record


@app.get("/books/filter")
def filter_books(
    genre: str = None,
    author: str = None,
    is_available: bool = None
):
    filtered = filter_books_logic(
        genre,
        author,
        is_available
    )

    return {
        "count": len(filtered),
        "books": filtered
    }

# -----------------------------------
# DAY 4 CRUD
# -----------------------------------

@app.post("/books")
def add_book(book: NewBook, response: Response):

    for b in books:
        if b["title"].lower() == book.title.lower():
            return {"error": "Duplicate title"}

    new_book = {
        "id": len(books) + 1,
        **book.dict()
    }

    books.append(new_book)

    response.status_code = 201

    return new_book


@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    genre: str = None,
    is_available: bool = None
):
    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    if genre is not None:
        book["genre"] = genre

    if is_available is not None:
        book["is_available"] = is_available

    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    books.remove(book)

    return {
        "message": f"{book['title']} deleted successfully"
    }

# -----------------------------------
# DAY 5 WORKFLOW
# -----------------------------------

@app.post("/queue/add")
def add_queue(member_name: str, book_id: int):

    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    if book["is_available"]:
        return {"error": "Book is available"}

    queue_item = {
        "member_name": member_name,
        "book_id": book_id
    }

    queue.append(queue_item)

    return {
        "message": "Added to queue",
        "queue_item": queue_item
    }


@app.get("/queue")
def get_queue():
    return {
        "total": len(queue),
        "queue": queue
    }


@app.post("/return/{book_id}")
def return_book(book_id: int):

    global record_counter

    book = find_book(book_id)

    if not book:
        return {"error": "Book not found"}

    book["is_available"] = True

    waiting = None

    for q in queue:
        if q["book_id"] == book_id:
            waiting = q
            break

    if waiting:

        book["is_available"] = False

        record = {
            "record_id": record_counter,
            "member_name": waiting["member_name"],
            "book_title": book["title"],
            "due_date": calculate_due_date(7)
        }

        borrow_records.append(record)

        queue.remove(waiting)

        record_counter += 1

        return {
            "message": "Returned and reassigned",
            "record": record
        }

    return {
        "message": "Returned and available"
    }

# -----------------------------------
# DAY 6
# -----------------------------------

@app.get("/books/search")
def search_books(keyword: str):

    results = [
        book for book in books
        if keyword.lower() in book["title"].lower()
        or keyword.lower() in book["author"].lower()
    ]

    return {
        "total_found": len(results),
        "results": results
    }


@app.get("/books/sort")
def sort_books(
    sort_by: str = "title",
    order: str = "asc"
):

    valid = ["title", "author", "genre"]

    if sort_by not in valid:
        return {"error": "Invalid sort_by"}

    if order not in ["asc", "desc"]:
        return {"error": "Invalid order"}

    reverse = order == "desc"

    sorted_books = sorted(
        books,
        key=lambda x: x[sort_by],
        reverse=reverse
    )

    return {
        "sort_by": sort_by,
        "order": order,
        "books": sorted_books
    }


@app.get("/books/page")
def paginate_books(
    page: int = Query(1, ge=1),
    limit: int = Query(3, ge=1)
):

    start = (page - 1) * limit
    end = start + limit

    total_pages = ceil(len(books) / limit)

    return {
        "page": page,
        "limit": limit,
        "total": len(books),
        "total_pages": total_pages,
        "books": books[start:end]
    }


@app.get("/borrow-records/search")
def search_records(member_name: str):

    results = [
        r for r in borrow_records
        if member_name.lower() in r["member_name"].lower()
    ]

    return {
        "count": len(results),
        "records": results
    }


@app.get("/borrow-records/page")
def paginate_records(
    page: int = 1,
    limit: int = 2
):

    start = (page - 1) * limit
    end = start + limit

    total_pages = ceil(len(borrow_records) / limit)

    return {
        "page": page,
        "total_pages": total_pages,
        "records": borrow_records[start:end]
    }


@app.get("/books/browse")
def browse_books(
    keyword: str = None,
    sort_by: str = "title",
    order: str = "asc",
    page: int = 1,
    limit: int = 3
):

    data = books

    if keyword:
        data = [
            book for book in data
            if keyword.lower() in book["title"].lower()
            or keyword.lower() in book["author"].lower()
        ]

    reverse = order == "desc"

    data = sorted(
        data,
        key=lambda x: x[sort_by],
        reverse=reverse
    )

    start = (page - 1) * limit
    end = start + limit

    total_pages = ceil(len(data) / limit)

    return {
        "keyword": keyword,
        "sort_by": sort_by,
        "order": order,
        "page": page,
        "limit": limit,
        "total": len(data),
        "total_pages": total_pages,
        "results": data[start:end]
    }