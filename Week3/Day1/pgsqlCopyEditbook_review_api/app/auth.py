import logging
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from passlib.hash import bcrypt
from jose import jwt
from datetime import datetime, timedelta
from database import get_db_connection
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
router = APIRouter()


class User(BaseModel):
    username: str
    password: str


# -- Register Admin ------------------------------------------------------------------------------------------
@router.post("/admin/register")
async def register_admin(user: User):
    conn = get_db_connection()
    cur = conn.cursor()

    # Check if user exists
    cur.execute("SELECT id FROM admins WHERE username = %s;", (user.username,))
    if cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash password
    hashed_password = bcrypt.hash(user.password)


    # Insert user
    cur.execute("INSERT INTO admins (username, password) VALUES (%s, %s);", (user.username, hashed_password))
    conn.commit()
    cur.close()
    conn.close()

    logger.info(f"Registered user: {user.username}")
    return {"message": "User registered successfully"}

# -- LOGIN Admin ------------------------------------------------------------------------------------------
@router.post("/admin/login")
async def login_admin(user: User):
    conn = get_db_connection()
    cur = conn.cursor()

    # Get user from DB
    cur.execute("SELECT id, password FROM admins WHERE username = %s;", (user.username,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=401, detail="Invalid username")

    user_id, stored_password = row

    if not bcrypt.verify(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Wrong password")


    # Create JWT token
    payload = {
        "id": user_id,
        "username": user.username,
        "isAdmin": True,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    logger.info(f"User logged in: {user.username}")
    return {"access_token": token, "token_type": "bearer"}




# -- Register User ------------------------------------------------------------------------------------------
@router.post("/register")
async def register_admin(user: User):
    conn = get_db_connection()
    cur = conn.cursor()

    # Check if user exists
    cur.execute("SELECT id FROM users WHERE username = %s;", (user.username,))
    if cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash password
    hashed_password = bcrypt.hash(user.password)


    # Insert user
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (user.username, hashed_password))
    conn.commit()
    cur.close()
    conn.close()

    logger.info(f"Registered user: {user.username}")
    return {"message": "User registered successfully"}


# -- LOGIN Admin ------------------------------------------------------------------------------------------
@router.post("/login")
async def login_admin(user: User):
    conn = get_db_connection()
    cur = conn.cursor()

    # Get user from DB
    cur.execute("SELECT id, password FROM users WHERE username = %s;", (user.username,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=401, detail="Invalid username")

    user_id, stored_password = row

    if not bcrypt.verify(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Wrong password")


    # Create JWT token
    payload = {
        "id": user_id,
        "username": user.username,
        "isAdmin": False,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    logger.info(f"User logged in: {user.username}")
    return {"access_token": token, "token_type": "bearer"}

    
