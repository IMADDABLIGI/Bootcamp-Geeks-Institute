from fastapi import Depends, Request, HTTPException
from jose import JWTError, jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# JWT settings
SECRET_KEY = "MacBook Air is better than Pro"
ALGORITHM = "HS256"

# FastAPI built-in security scheme
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # You can return full payload or just user info
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    

if __name__ == "__main__":
    pass
