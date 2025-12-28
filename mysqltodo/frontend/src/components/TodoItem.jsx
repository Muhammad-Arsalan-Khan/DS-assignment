import { useState } from 'react';

const TodoItem = ({ todo, onUpdate, onDelete }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(todo.title);

  const handleToggle = () => {
    onUpdate(todo.id, { completed: !todo.completed });
  };

  const handleEdit = () => {
    if (isEditing) {
      onUpdate(todo.id, { title });
    }
    setIsEditing(!isEditing);
  };

  const handleDelete = () => {
    onDelete(todo.id);
  };

  return (
    <li>
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={handleToggle}
      />
      {isEditing ? (
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      ) : (
        <span style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}>
          {todo.title}
        </span>
      )}
      <button onClick={handleEdit}>{isEditing ? 'Save' : 'Edit'}</button>
      <button onClick={handleDelete}>Delete</button>
    </li>
  );
};

export default TodoItem;