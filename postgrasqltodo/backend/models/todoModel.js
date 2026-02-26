import client from '../config/db.js';

class TodoModel {
  // CREATE
  static async create(title) {
    const result = await client.query(
      'INSERT INTO todos (title, completed, created_at) VALUES ($1, $2, NOW()) RETURNING id',
      [title, false]
    );
    return result.rows[0].id; // naya id return karega
  }

  // READ ALL
  static async findAll() {
    const result = await client.query('SELECT * FROM todos ORDER BY created_at DESC');
    return result.rows;
  }

  // READ SINGLE BY ID
  static async findById(id) {
    const result = await client.query('SELECT * FROM todos WHERE id = $1', [id]);
    return result.rows[0]; // ek hi row return hogi
  }

  // UPDATE BY ID
  static async update(id, title, completed) {
    await client.query(
      'UPDATE todos SET title = $1, completed = $2 WHERE id = $3',
      [title, completed, id]
    );
  }

  // DELETE BY ID
  static async delete(id) {
    await client.query('DELETE FROM todos WHERE id = $1', [id]);
  }
}

export default TodoModel;