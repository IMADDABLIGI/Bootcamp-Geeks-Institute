from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, conint
from typing import List
from middleware import verify_token
from database import get_db_connection

router = APIRouter()

class Review(BaseModel):
    book_id: int
    rate: conint(ge=0, le=10)  # Validate rate between 0 and 10

class ReviewOut(Review):
    review_id: int
    user_id: int

# -- CREATE REVIEW --
@router.post("/reviews")
def create_review(review: Review, payload: dict = Depends(verify_token)):
    user_id = payload["id"]
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO reviews (book_id, user_id, rate)
        VALUES (%s, %s, %s);
        """,
        (review.book_id, user_id, review.rate)
    )
    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Review has been created successfully"}


# -- READ ALL REVIEWS --
@router.get("/reviews", response_model=List[ReviewOut])
def read_reviews():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT review_id, book_id, user_id, rate FROM reviews;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {"review_id": r[0], "book_id": r[1], "user_id": r[2], "rate": r[3]}
        for r in rows
    ]


# -- UPDATE REVIEW (Only Owner) --
@router.put("/reviews/{review_id}")
def update_review(review_id: int, review: Review, payload: dict = Depends(verify_token)):
    user_id = payload["id"]
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT user_id FROM reviews WHERE review_id = %s;", (review_id,))
    row = cur.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Review not found")
    if row[0] != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this review")

    cur.execute(
        "UPDATE reviews SET rate = %s, book_id = %s WHERE review_id = %s;",
        (review.rate, review.book_id, review_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Review updated successfully"}


# -- DELETE REVIEW (Only Owner) --
@router.delete("/reviews/{review_id}")
def delete_review(review_id: int, payload: dict = Depends(verify_token)):
    user_id = payload["id"]
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT user_id FROM reviews WHERE review_id = %s;", (review_id,))
    row = cur.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Review not found")
    if row[0] != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this review")

    cur.execute("DELETE FROM reviews WHERE review_id = %s;", (review_id,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Review deleted successfully"}

@router.delete("/admin/reviews/{review_id}")
def delete_review_admin(review_id: int, payload: dict = Depends(verify_token)):
    if not payload.get("isAdmin"):
        raise HTTPException(status_code=403, detail="Admin privileges required")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT review_id FROM reviews WHERE review_id = %s;", (review_id,))
    row = cur.fetchone()

    if not row:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Review not found")

    cur.execute("DELETE FROM reviews WHERE review_id = %s;", (review_id,))
    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Review deleted successfully by admin"}
