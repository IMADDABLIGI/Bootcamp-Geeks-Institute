from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from passlib.hash import bcrypt
from middleware import verify_token
from database import get_db_connection  # assuming you moved the db fn to db.py
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

class AdminUser(BaseModel):
    username: str
    password: str

@router.post("/admin/create-user")
async def admin_create_user(new_user: AdminUser, payload: dict = Depends(verify_token)):
    if not payload.get("isAdmin"):
        raise HTTPException(status_code=403, detail="Admin privileges required")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s;", (new_user.username,))
    if cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = bcrypt.hash(new_user.password)

    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (new_user.username, hashed_password))
    conn.commit()
    cur.close()
    conn.close()

    logger.info(f"Admin created user: {new_user.username}")
    return {"message": f"User '{new_user.username}' created successfully"}

@router.delete("/admin/delete-user/{user_id}")
async def admin_delete_user(user_id: int, payload: dict = Depends(verify_token)):
    if not payload.get("isAdmin"):
        raise HTTPException(status_code=403, detail="Admin privileges required")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE id = %s;", (user_id,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="User not found")

    cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

    logger.info(f"Admin deleted user with ID: {user_id}")
    return {"message": f"User with ID {user_id} deleted successfully"}
