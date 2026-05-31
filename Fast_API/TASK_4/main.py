from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# -----------------------------
# PRODUCTS DATABASE
# -----------------------------

products = {
    1: {
        "name": "Wireless Mouse",
        "price": 499,
        "in_stock": True
    },
    2: {
        "name": "Notebook",
        "price": 99,
        "in_stock": True
    },
    3: {
        "name": "USB Hub",
        "price": 799,
        "in_stock": False
    },
    4: {
        "name": "Pen Set",
        "price": 49,
        "in_stock": True
    }
}

# -----------------------------
# STORAGE
# -----------------------------

cart = []
orders = []

# -----------------------------
# Pydantic Model
# -----------------------------

class Checkout(BaseModel):
    customer_name: str
    delivery_address: str

# -----------------------------
# Helper Function
# -----------------------------

def calculate_total(product, quantity):
    return product["price"] * quantity

# -----------------------------
# HOME
# -----------------------------

@app.get("/")
def home():
    return {"message": "Cart System API Running"}

# -----------------------------
# GET PRODUCTS
# -----------------------------

@app.get("/products")
def get_products():
    return products

# -----------------------------
# ADD TO CART
# -----------------------------

@app.post("/cart/add")
def add_to_cart(product_id: int, quantity: int = 1):

    # Product exists or not
    if product_id not in products:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product = products[product_id]

    # Stock check
    if not product["in_stock"]:
        raise HTTPException(
            status_code=400,
            detail=f"{product['name']} is out of stock"
        )

    # Already exists in cart
    for item in cart:
        if item["product_id"] == product_id:
            item["quantity"] += quantity
            item["subtotal"] = calculate_total(product, item["quantity"])

            return {
                "message": "Cart updated",
                "cart_item": item
            }

    # New cart item
    cart_item = {
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "subtotal": calculate_total(product, quantity)
    }

    cart.append(cart_item)

    return {
        "message": "Added to cart",
        "cart_item": cart_item
    }

# -----------------------------
# VIEW CART
# -----------------------------

@app.get("/cart")
def view_cart():

    if not cart:
        return {"message": "Cart is empty"}

    grand_total = sum(item["subtotal"] for item in cart)

    return {
        "items": cart,
        "item_count": len(cart),
        "grand_total": grand_total
    }

# -----------------------------
# REMOVE ITEM
# -----------------------------

@app.delete("/cart/{product_id}")
def remove_from_cart(product_id: int):

    for item in cart:
        if item["product_id"] == product_id:
            cart.remove(item)

            return {
                "message": "Item removed from cart",
                "removed_item": item
            }

    raise HTTPException(
        status_code=404,
        detail="Item not found in cart"
    )

# -----------------------------
# CHECKOUT
# -----------------------------

@app.post("/cart/checkout")
def checkout(data: Checkout):

    if not cart:
        raise HTTPException(
            status_code=400,
            detail="Cart is empty — add items first"
        )

    grand_total = sum(item["subtotal"] for item in cart)

    placed_orders = []

    for item in cart:

        order = {
            "order_id": len(orders) + 1,
            "customer_name": data.customer_name,
            "delivery_address": data.delivery_address,
            "product": item["product_name"],
            "quantity": item["quantity"],
            "total_price": item["subtotal"]
        }

        orders.append(order)
        placed_orders.append(order)

    cart.clear()

    return {
        "message": "Checkout successful",
        "orders_placed": placed_orders,
        "grand_total": grand_total
    }

# -----------------------------
# VIEW ORDERS
# -----------------------------

@app.get("/orders")
def get_orders():

    return {
        "orders": orders,
        "total_orders": len(orders)
    }