# Blog API

A RESTful API for a blog platform built with Node.js, Express, and PostgreSQL.

## Features

- Full CRUD operations for blog posts
- PostgreSQL database integration
- Input validation and error handling
- Clean MVC architecture
- Environment-based configuration
- CORS support

## Project Structure

```
blog-api/
├── server.js              # Main server file
├── package.json           # Dependencies and scripts
├── .env                   # Environment variables
├── README.md             # Project documentation
├── database/
│   └── init.sql          # Database initialization script
├── config/
│   └── database.js       # Database configuration
├── controllers/
│   └── postController.js # Post controller logic
├── models/
│   └── Post.js          # Post model
└── routes/
    └── posts.js         # Post routes
```

## Setup Instructions

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up PostgreSQL database:**
   - Create a new database named `blog_db`
   - Run the SQL script from `database/init.sql`

3. **Configure environment variables:**
   - Update `.env` with your database credentials

4. **Start the server:**
   ```bash
   npm run dev  # Development mode
   npm start    # Production mode
   ```

## API Endpoints

- GET /api/posts - Get all posts
- GET /api/posts/:id - Get single post
- POST /api/posts - Create new post
- PUT /api/posts/:id - Update post
- DELETE /api/posts/:id - Delete post

Visit http://localhost:3000 for full API documentation.
