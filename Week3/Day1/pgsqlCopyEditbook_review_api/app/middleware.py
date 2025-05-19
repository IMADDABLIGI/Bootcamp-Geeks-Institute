from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from database import get_db_connection  # Import your DB connection function from its actual file
# from config import SECRET_KEY, ALGORITHM  # Adjust if needed

SECRET_KEY = "MacBook Air is better than Pro"
ALGORITHM = "HS256"

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        is_admin = payload.get("isAdmin")

        if user_id is None or is_admin is None:
            raise HTTPException(status_code=400, detail="Invalid token payload")

        # Check user existence based on admin status
        conn = get_db_connection()
        cur = conn.cursor()

        if is_admin:
            cur.execute("SELECT id FROM admins WHERE id = %s;", (user_id,))
        else:
            cur.execute("SELECT id FROM users WHERE id = %s;", (user_id,))

        if not cur.fetchone():
            role = "admin" if is_admin else "user"
            raise HTTPException(status_code=403, detail=f"{role.capitalize()} not found in database")

        cur.close()
        conn.close()

        return payload

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
