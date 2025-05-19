# 📚 Book Review API

A simple FastAPI backend for managing users, books, and reviews, with role-based access control (admin and regular users). Admins can manage users and bypass ownership checks on resources.

## 🗂 Project Structure

```
project-root/
│
├── app/
│   ├── main.py              # Entry point for FastAPI app
│   ├── auth.py              # Authentication routes (/register, /login)
│   ├── books_crud.py        # CRUD operations for books
│   ├── reviews_crud.py      # CRUD operations for reviews
│   ├── admin_routes.py      # Admin-only routes (create/delete users)
│   ├── middleware.py        # JWT token verification logic
│   ├── config.py            # Configuration (e.g. secret keys, env handling)
│   └── database.py          # DB connection setup
│
├── env/                     # Virtual environment (do not edit)
├── requirements.txt         # Python dependencies
└── README.md                # You're reading this file!
```

---

## ⚙️ Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # or use `env\Scripts\activate` on Windows
   ```

3. **Start the FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Test API using [Postman](https://www.postman.com/) or [httpie](https://httpie.io/)**

---

## 🧪 How to Test the API

### 🔑 1. Create an Admin

**Endpoint:** `POST /admin/register`  
**Body:**
```json
{
  "username": "admin123",
  "password": "secret123"
}
```

### 🔐 2. Login as Admin and Get Access Token

**Endpoint:** `POST /admin/login`  
**Body:**
```json
{
  "username": "admin123",
  "password": "secret123"
}
```

**Response:**
```json
{
  "access_token": "YOUR_JWT_TOKEN",
  "token_type": "bearer"
}
```

### 👤 3. Create a Normal User

**Endpoint:** `POST /admin/create-user`  
**Headers:**
```http
Authorization: Bearer YOUR_JWT_TOKEN
```

**Body:**
```json
{
  "username": "user1",
  "password": "pass123"
}
```

### 👋 4. Or Let the User Register Themselves

**Endpoint:** `POST /register`  
**Body:**
```json
{
  "username": "user1",
  "password": "pass123"
}
```

### 🔓 5. User Login

**Endpoint:** `POST /login`  
**Body:**
```json
{
  "username": "user1",
  "password": "pass123"
}
```

---

## 🔁 User CRUD for Books

### ➕ Create Book
**POST /books**  
**Headers:** Bearer token required  
**Body:**
```json
{
  "title": "Clean Code"
}
```

### 📖 Read All Books
**GET /books**

### ✏️ Update Book (Owner Only)
**PUT /books/{book_id}**  
**Body:**
```json
{
  "title": "Refactored Title"
}
```

### ❌ Delete Book (Owner Only)
**DELETE /books/{book_id}**

### ❌ Delete Book (Admin)
**DELETE /admin/books/{book_id}**

---

## ⭐ Review CRUD

### ➕ Create Review
**POST /reviews**  
**Body:**
```json
{
  "book_id": 1,
  "rate": 9
}
```

> 🔒 Rate must be between 0 and 10.

### ❌ Delete Review (Owner Only)
**DELETE /reviews/{review_id}**

### ❌ Delete Review (Admin)
**DELETE /admin/reviews/{review_id}**

---

## ❌ Delete a User (Admin Only)

**DELETE /admin/delete-user/{user_id}**  
**Headers:** Bearer admin token

---

## 📌 Notes

- Token must be passed in the `Authorization` header for protected routes.
- Admins have full control; regular users can only modify their own books/reviews.

---

## 📬 Contact

For improvements or questions, feel free to reach out.

Happy coding! 🚀
