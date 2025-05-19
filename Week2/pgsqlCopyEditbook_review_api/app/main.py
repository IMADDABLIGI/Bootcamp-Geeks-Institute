import logging
import psycopg2
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict
import bcrypt
from jose import jwt
from datetime import datetime, timedelta
from middleware import verify_token

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# users_db: Dict[str, bytes] = {}

SECRET_KEY = "MacBook Air is better than Pro"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

HOSTNAME = 'localhost'
USERNAME = 'hicham'
PASSWORD = 'root'
DATABASE = 'BooksReviews'

class User(BaseModel):
    username: str
    password: str

def get_db_connection():
    return psycopg2.connect(
        host=HOSTNAME,
        user=USERNAME,
        password=PASSWORD,
        dbname=DATABASE
    )


@app.get("/")
async def welcome(payload: dict = Depends(verify_token)):
    return {
        "Hello": "World",
        "user": {
            "id": payload["id"],
            "username": payload["username"],
            "isAdmin": payload["isAdmin"]
        }
    }

# -- Register USER ------------------------------------------------------------------------------------------
@app.post("/register")
async def register(user: User):
    conn = get_db_connection()
    cur = conn.cursor()

    # Check if user exists
    cur.execute("SELECT id FROM users WHERE username = %s;", (user.username,))
    if cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash password
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Insert user
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (user.username, hashed_password))
    conn.commit()
    cur.close()
    conn.close()

    logger.info(f"Registered user: {user.username}")
    return {"message": "User registered successfully"}

# -- LOGIN USER ------------------------------------------------------------------------------------------
@app.post("/login")
async def login(user: User):
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

    if not bcrypt.checkpw(user.password.encode('utf-8'), stored_password.encode('utf-8')):
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










if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=4567)
