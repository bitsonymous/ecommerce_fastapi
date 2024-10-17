# app/main.py

from fastapi import FastAPI
from app.routers import products, categories, carts, users, auth, accounts  # Import all routers

# API description for the FastAPI docs
description = """
Welcome to the E-commerce API! 🚀

This API provides a comprehensive set of functionalities for managing your e-commerce platform.

repo : 

"""

# Initialize FastAPI application
app = FastAPI(
    description=description,
    title="E-commerce API",
    version="1.0.0",
    contact={
        "name": "Ali Seyedi",
        "url": "https://github.com/aliseyedi01",
    },
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",
        "layout": "BaseLayout",
        "filter": True,
        "tryItOutEnabled": True,
        "onComplete": "Ok"
    },
)

# Include routers for different modules
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(carts.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(auth.router)

# Optional: You can add a root endpoint for quick checks
@app.get("/")
async def root():
    return {"message": "Welcome to the E-commerce API!"}
