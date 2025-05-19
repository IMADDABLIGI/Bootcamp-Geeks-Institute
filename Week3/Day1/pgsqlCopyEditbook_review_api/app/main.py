import logging
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from middleware import verify_token
from database import get_db_connection
# from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from auth import router as auth_router
from admin_routes import router as admin_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(auth_router)
app.include_router(admin_router)

# users_db: Dict[str, bytes] = {}

class User(BaseModel):
    username: str
    password: str

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



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=4567)
