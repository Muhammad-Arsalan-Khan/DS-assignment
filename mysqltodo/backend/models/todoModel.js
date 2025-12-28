import pool from '../config/db.js';

// console.log(pool)


// await pool.query(`
//   CREATE TABLE IF NOT EXISTS todos (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     title VARCHAR(255) NOT NULL,
//     completed BOOLEAN DEFAULT FALSE,
//     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
//   )
// `);


class TodoModel {
  static async create(title) {
    const [result] = await pool.execute(
      'INSERT INTO todos (title, completed, created_at) VALUES (?, ?, NOW())',
      [title, false]
    );
    return result.insertId;
  }

  static async findAll() {
    const [rows] = await pool.execute('SELECT * FROM todos ORDER BY created_at DESC');
    return rows;
  }

  static async findById(id) {
    const [rows] = await pool.execute('SELECT * FROM todos WHERE id = ?', [id]);
    return rows[0];
  }

  static async update(id, title, completed) {
    await pool.execute(
      'UPDATE todos SET title = ?, completed = ? WHERE id = ?',
      [title, completed, id]
    );
  }

  static async delete(id) {
    await pool.execute('DELETE FROM todos WHERE id = ?', [id]);
  }
}

export default TodoModel;