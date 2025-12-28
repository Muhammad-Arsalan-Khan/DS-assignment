import TodoModel from '../models/todoModel.js';

class TodoController {
  static async createTodo(req, res) {
    try {
      const { title } = req.body;
      if (!title) {
        return res.status(400).json({ error: 'Title is required' });
      }
      const id = await TodoModel.create(title);
      res.status(201).json({ id, title, completed: false, message: 'Todo created successfully' });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }

  static async getAllTodos(req, res) {
    try {
      const todos = await TodoModel.findAll();
    //   console.log("hello",todos);
      if (!todos) {
        return res.status(200).json({ error: 'no record here' });
      }
      res.status(200).json(todos);
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }

  static async getTodoById(req, res) {
    try {
      const { id } = req.params;
      const todo = await TodoModel.findById(id);
      if (!todo) {
        return res.status(404).json({ error: 'Todo not found' });
      }
      res.status(200).json(todo);
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }

  static async updateTodo(req, res) {
    try {
      const { id } = req.params;
      const { title, completed } = req.body;
      const todo = await TodoModel.findById(id);
      if (!todo) {
        return res.status(404).json({ error: 'Todo not found' });
      }
      await TodoModel.update(id, title !== undefined ? title : todo.title, completed !== undefined ? completed : todo.completed);
      res.status(200).json({ message: 'Todo updated successfully' });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }

  static async deleteTodo(req, res) {
    try {
      const { id } = req.params;
      const todo = await TodoModel.findById(id);
      if (!todo) {
        return res.status(404).json({ error: 'Todo not found' });
      }
      await TodoModel.delete(id);
      res.status(200).json({ message: 'Todo deleted successfully' });
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: 'Internal server error' });
    }
  }
}

export default TodoController;