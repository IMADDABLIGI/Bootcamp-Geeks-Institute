import logging
from fastapi import FastAPI, HTTPException
from users import users
from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str

class UserDeleteRequest(BaseModel):
    user_id: int

# Configure logging - helps with debugging and monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()



@app.get("/users")
async def get_users():
    try:
        result = users.read_all()
        # logger.info("Test")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/users/{user_id}")
async def get_user(user_id):
    try:
        result = users.read(user_id)
        # logger.info(result)

        if not result:
            raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/users/register")
async def create_user(data: UserCreate):
    try:
        result = users.create(data.first_name, data.last_name)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/users/")
async def delete_user(data: UserDeleteRequest):
    try:
        result = users.delete(data.user_id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/users/{user_id}")
async def update_user(user_id: int, first_name: str, last_name: str):
    try:
        result = users.update(first_name, last_name, user_id)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=4567)
