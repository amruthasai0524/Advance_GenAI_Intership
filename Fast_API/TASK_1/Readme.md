# FastAPI Day 1 Assignment

## 📌 Project Overview

This project is a beginner-friendly FastAPI application created as part of the FastAPI Internship Assignment.

The project demonstrates:

* FastAPI basics
* API endpoint creation
* Product filtering
* Search functionality
* Store summary generation
* JSON responses
* Swagger UI documentation

---

# 🚀 Technologies Used

* Python
* FastAPI
* Uvicorn

---

# 📂 Project Structure

```bash
ASSIGNMENT 1
│
├── main.py
├── Q1_Output.png
├── Q2_Output.png
├── Q3_Output.png
├── Q4_Output.png
├── Q5_Output.png
└── Bonus_Output.png
```

---

# ▶️ How to Run the Project

## Step 1 — Install FastAPI & Uvicorn

```bash
pip install fastapi uvicorn
```

---

## Step 2 — Run the Server

```bash
uvicorn main:app --reload
```

---

## Step 3 — Open Swagger UI

Open browser and visit:

```bash
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

| Method | Endpoint                             | Description                       |
| ------ | ------------------------------------ | --------------------------------- |
| GET    | `/`                                  | Home Route                        |
| GET    | `/products`                          | Get All Products                  |
| GET    | `/products/category/{category_name}` | Filter Products by Category       |
| GET    | `/products/instock`                  | Show In-Stock Products            |
| GET    | `/store/summary`                     | Store Summary                     |
| GET    | `/products/search/{keyword}`         | Search Products                   |
| GET    | `/products/deals`                    | Cheapest & Most Expensive Product |

---

# 📸 Screenshots

## Q1 Output

Shows all products and total product count.

## Q2 Output

Shows products filtered by category.

## Q3 Output

Shows only in-stock products.

## Q4 Output

Displays store summary including:

* Total products
* In-stock products
* Out-of-stock products
* Categories

## Q5 Output

Shows searched products using keyword search.

## Bonus Output

Displays:

* Cheapest product
* Most expensive product

---

# ✅ Features Implemented

* Product Management API
* Category Filtering
* Product Search
* Store Analytics
* In-Stock Product Filtering
* FastAPI Swagger Documentation

---

# 🎯 Learning Outcomes

Through this assignment, I learned:

* FastAPI fundamentals
* REST API development
* API testing using Swagger UI
* Handling JSON responses
* Python list filtering
* Building backend APIs

---

# 👩‍💻 Author

Amrutha Reddy

