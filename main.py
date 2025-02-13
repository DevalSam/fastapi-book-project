from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}

# Book model
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

# Sample book data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "description": "Description 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2", "description": "Description 2"},
]

# Endpoint to get a book by ID
@app.get("/api/v1/{book_id}", response_model=Book)
def get_book(book_id: int):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book