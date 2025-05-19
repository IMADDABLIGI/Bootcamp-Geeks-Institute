from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from middleware import verify_token
from database import get_db_connection  # <- your DB connection function

router = APIRouter()

class Book(BaseModel):
    title: str

class BookOut(Book):
    books_id: int
    user_id: int

# -- CREATE BOOK --
@router.post("/books")
def create_book(book: Book, payload: dict = Depends(verify_token)):
    user_id = payload["id"]
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO books (title, user_id) VALUES (%s, %s);",
        (book.title, user_id)
    )
    # book_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Book has been created successfully"}


# -- READ ALL BOOKS --
@router.get("/books", response_model=List[BookOut])
def read_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT books_id, title, user_id FROM books;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"books_id": r[0], "title": r[1], "user_id": r[2]} for r in rows]


# -- UPDATE BOOK (Only Owner) --
@router.put("/books/{book_id}")
def update_book(book_id: int, book: Book, payload: dict = Depends(verify_token)):
    user_id = payload["id"]
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT user_id FROM books WHERE books_id = %s;", (book_id,))
    row = cur.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    if row[0] != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this book")

    cur.execute("UPDATE books SET title = %s WHERE books_id = %s;", (book.title, book_id))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Book updated successfully"}


# -- DELETE BOOK (Only Owner) --
@router.delete("/books/{book_id}")
def delete_book(book_id: int, payload: dict = Depends(verify_token)):
    user_id = payload["id"]
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT user_id FROM books WHERE books_id = %s;", (book_id,))
    row = cur.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    if row[0] != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this book")

    cur.execute("DELETE FROM books WHERE books_id = %s;", (book_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Book deleted successfully"}

# -- DELETE BOOK (Admin) --
@router.delete("/admin/books/{book_id}")
def delete_book(book_id: int, payload: dict = Depends(verify_token)):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT user_id FROM books WHERE books_id = %s;", (book_id,))
    row = cur.fetchone()

    if not payload.get("isAdmin"):
        raise HTTPException(status_code=403, detail="Admin privileges required")
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")

    cur.execute("DELETE FROM books WHERE books_id = %s;", (book_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Book deleted successfully"}