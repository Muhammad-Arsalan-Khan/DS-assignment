# Todo Backend

This is the backend for the Todo application built with Node.js, Express.js, and MySQL.

## Setup

1. Install dependencies:
   ```
   npm install
   ```

2. Set up MySQL database:
   - Ensure MySQL server is running.
   - Update the database configuration in `config/db.js` with your MySQL credentials (host, user, password).
   - Run the setup script to create the database and table:
     ```
     node setup.js
     ```
   - Alternatively, manually create the database and table:
     - Create a database named `todo_db`.
     - Run the following SQL query to create the `todos` table:
       ```sql
       CREATE TABLE todos (
         id INT AUTO_INCREMENT PRIMARY KEY,
         title VARCHAR(255) NOT NULL,
         completed BOOLEAN DEFAULT FALSE,
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       );
       ```

3. Start the server:
   ```
   npm start
   ```
   or for development:
   ```
   npm run dev
   ```

The server will run on http://localhost:3000.

## API Endpoints

- `GET /api/todos` - Get all todos
- `GET /api/todos/:id` - Get a single todo
- `POST /api/todos` - Create a new todo
- `PUT /api/todos/:id` - Update a todo
- `DELETE /api/todos/:id` - Delete a todo