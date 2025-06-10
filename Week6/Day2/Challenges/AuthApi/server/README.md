# User Management API

A complete user management system with registration, login, and CRUD operations built with Express.js, MySQL, and bcrypt.

## Features

- User registration with password hashing
- User login with password verification
- Get all users
- Get user by ID
- Update user information
- Transaction-based database operations
- Input validation and error handling

## Database Structure

### Tables
- `users`: id, email, username, first_name, last_name, created_at, updated_at
- `hashpwd`: id, username, password, created_at

## API Endpoints

### POST /api/register
Register a new user
```json
{
  "email": "user@example.com",
  "username": "john_doe",
  "first_name": "John",
  "last_name": "Doe",
  "password": "securepassword"
}
```

### POST /api/login
Login user
```json
{
  "username": "john_doe",
  "password": "securepassword"
}
```

### GET /api/users
Get all users

### GET /api/users/:id
Get user by ID

### PUT /api/users/:id
Update user information
```json
{
  "email": "newemail@example.com",
  "first_name": "John",
  "last_name": "Smith",
  "password": "newpassword" // optional
}
```

## Setup Instructions

1. Make sure MySQL is installed and running
2. Create a database named 'Auth'
3. Update .env file with your database credentials
4. Install dependencies: `npm install`
5. Initialize database tables: `node init-db.js`
6. Start the server: `npm start` or `npm run dev`

## Testing with curl

### Register a user:
```bash
curl -X POST http://localhost:3000/api/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","username":"testuser","first_name":"Test","last_name":"User","password":"password123"}'
```

### Login:
```bash
curl -X POST http://localhost:3000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"password123"}'
```

### Get all users:
```bash
curl http://localhost:3000/api/users
```

### Get user by ID:
```bash
curl http://localhost:3000/api/users/1
```

### Update user:
```bash
curl -X PUT http://localhost:3000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"email":"updated@example.com","first_name":"Updated","last_name":"User"}'
```
