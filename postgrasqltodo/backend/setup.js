import mysql from 'mysql2/promise';

async function setupDatabase() {
  try {
    // Connect without specifying database
    const connection = await mysql.createConnection({
      host: 'localhost',
      user: 'root',
      password: 'admin'
    });

    // Create database if not exists
    await connection.execute('CREATE DATABASE IF NOT EXISTS todo_db');

    // Use the database
    await connection.execute('USE todo_db');

    // Create table if not exists
    await connection.execute(`
      CREATE TABLE IF NOT EXISTS todos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        completed BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `);

    console.log('Database and table created successfully');
    await connection.end();
  } catch (error) {
    console.error('Error setting up database:', error);
  }
}

setupDatabase();