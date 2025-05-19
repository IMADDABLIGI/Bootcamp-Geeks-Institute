import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

users_db: Dict[str, str] = {}

class User(BaseModel):
    username: str
    password: str

@app.get("/")
async def welcome():
    return {"Hello": "World"}

@app.post("/register")
async def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    users_db[user.username] = user.password
    logger.info(f"Registered user: {user.username}")
    return {"message": "User registered successfully"}

@app.post("/login")
async def login(user: User):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    logger.info(f"User logged in: {user.username}")
    return {"message": "Login successful"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=4567)
