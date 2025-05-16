import logging
from fastapi import FastAPI, HTTPException
from users import users
from user_passport import user_passport
from pydantic import BaseModel
from datetime import date



class UserCreate(BaseModel):
    first_name: str
    last_name: str

class UserDeleteRequest(BaseModel):
    user_id: int

class UserUpdateRequest(BaseModel):
    user_id: int
    first_name: str
    last_name: str

class PassportCreate(BaseModel):
    user_id: int
    nationality: str
    expire_date: date

class PassportDeleteRequest(BaseModel):
    passport_id: int

# Configure logging - helps with debugging and monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
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

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if not result:
            raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
        return result


@app.post("/users/register")
async def create_user(data: UserCreate):
    try:
        result = users.create(data.first_name, data.last_name)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/users")
async def delete_user(data: UserDeleteRequest):
    try:
        result = users.delete(data.user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if not result:
            raise HTTPException(status_code=404, detail=f"User with ID {data.user_id} not found")
        return {"message": result}

@app.post("/users/update")
async def update_user(data: UserUpdateRequest):
    try:
        result = users.update(data.user_id, data.first_name, data.last_name)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if not result:
            raise HTTPException(status_code=404, detail=f"User with ID {data.user_id} not found")
        return {"message": result}


# Passport-----------------------------------


@app.post("/passport/register")
async def create_passport(data: PassportCreate):
    try:
        result = user_passport.create(data.user_id, data.nationality, data.expire_date)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/passport")
async def read_all_passports():
    try:
        result = user_passport.read_all()
        return {"passports": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/passport/{user_id}")
async def read_passport(user_id: int):
    try:
        result = user_passport.read(user_id)
        if not result:
            raise HTTPException(status_code=404, detail="Passport not found for this user")
        return {"passport": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/passport")
async def delete_passport(data: PassportDeleteRequest):
    try:
        result = user_passport.delete(data.passport_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if not result:
            raise HTTPException(status_code=404, detail="Passport not found")
        return {"message": result}















if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=4567)
