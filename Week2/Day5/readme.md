# FastAPI User and Passport Management API

This project is a RESTful API built with FastAPI and PostgreSQL for managing users and their passport information. It supports CRUD operations on both users and their associated passports.

## 🛠 Tech Stack

- **FastAPI** – Web framework  
- **PostgreSQL** – Relational database  
- **Psycopg2** – PostgreSQL adapter for Python  
- **Uvicorn** – ASGI server  
- **Pydantic** – Data validation  

---

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone git@github.com:IMADDABLIGI/Bootcamp-Geeks-Institute.git
cd Bootcamp-Geeks-Institute
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn psycopg2 pydantic
```

### 3. Configure your database

Update your database connection info in `users.py` and `user_passport.py`:

```python
self.connect = psycopg2.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=PASSWORD,
    dbname=DATABASE
)
```

### 4. Run the server

```bash
python api.py
```

Or using Uvicorn:

```bash
uvicorn api:app --reload --port 4567
```

---

## 🌍 API Endpoints

### Root

- `GET /` – Test the API

---

## 👤 User Routes

### Get all users

```http
GET /users
```

### Get user by ID

```http
GET /users/{user_id}
```

### Create user

```http
POST /users/register
```

**JSON Body**:
```json
{
  "first_name": "John",
  "last_name": "Doe"
}
```

### Delete user

```http
DELETE /users
```

**JSON Body**:
```json
{
  "user_id": 1
}
```

### Update user

```http
POST /users/update
```

**JSON Body**:
```json
{
  "user_id": 1,
  "first_name": "Jane",
  "last_name": "Smith"
}
```

---

## 🛂 Passport Routes

### Create passport

```http
POST /passport/register
```

**JSON Body**:
```json
{
  "user_id": 1,
  "nationality": "Moroccan",
  "expire_date": "2028-06-11"
}
```

### Get all passports

```http
GET /passport
```

### Get passport by user ID

```http
GET /passport/{user_id}
```

### Delete passport

```http
DELETE /passport
```

**JSON Body**:
```json
{
  "passport_id": 1
}
```

---

## 🔗 Using ngrok (Optional)

To expose your local server for external testing:

```bash
ngrok http 4567
```

Copy the forwarded URL (e.g., `https://abc123.ngrok.io`) and use it in Postman.

---

## ✅ Notes

- Ensure PostgreSQL is running and tables are created.
- The `user_passport` table uses `user_id` as a foreign key with `ON DELETE CASCADE`.

---

## 📬 Feedback

If you encounter issues or have suggestions, feel free to open an issue or contribute!
