import TodoList from './todo.js';

const myTodos = new TodoList();

myTodos.addTask("Buy groceries");
myTodos.addTask("Finish coding exercise");
myTodos.addTask("Walk the dog");

myTodos.completeTask(1);

myTodos.listTasks();
