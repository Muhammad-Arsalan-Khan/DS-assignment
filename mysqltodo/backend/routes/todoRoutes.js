import express from 'express';
import TodoController from '../controllers/todoController.js';

const router = express.Router();

router.post('/', TodoController.createTodo);
router.get('/', TodoController.getAllTodos);
router.get('/:id', TodoController.getTodoById);
router.put('/:id', TodoController.updateTodo);
router.delete('/:id', TodoController.deleteTodo);

export default router;