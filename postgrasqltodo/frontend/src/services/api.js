import axios from 'axios';

const API_BASE_URL = 'http://localhost:3000/api/todos';

const api = {
  getAllTodos: () => axios.get(API_BASE_URL),
  getTodoById: (id) => axios.get(`${API_BASE_URL}/${id}`),
  createTodo: (todo) => axios.post(API_BASE_URL, todo),
  updateTodo: (id, todo) => axios.put(`${API_BASE_URL}/${id}`, todo),
  deleteTodo: (id) => axios.delete(`${API_BASE_URL}/${id}`)
};

export default api;