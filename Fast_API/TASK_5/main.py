from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# -----------------------------
# DATABASE
# -----------------------------

students = []

# -----------------------------
# Pydantic Model
# -----------------------------

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

# -----------------------------
# HOME
# -----------------------------

@app.get("/")
def home():
    return {"message": "Student Management API Running"}

# -----------------------------
# ADD STUDENT
# -----------------------------

@app.post("/students")
def add_student(student: Student):

    # Duplicate ID check
    for s in students:
        if s["id"] == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student.dict())

    return {
        "message": "Student added successfully",
        "student": student
    }

# -----------------------------
# GET ALL STUDENTS
# -----------------------------

@app.get("/students")
def get_students():

    return {
        "total_students": len(students),
        "students": students
    }

# -----------------------------
# GET SINGLE STUDENT
# -----------------------------

@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# -----------------------------
# UPDATE STUDENT
# -----------------------------

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student["id"] == student_id:

            students[index] = updated_student.dict()

            return {
                "message": "Student updated successfully",
                "updated_student": updated_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# -----------------------------
# DELETE STUDENT
# -----------------------------

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student deleted successfully",
                "deleted_student": student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )