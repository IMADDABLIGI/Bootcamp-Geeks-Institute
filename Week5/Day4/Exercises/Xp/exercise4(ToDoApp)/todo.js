class TodoList {
  constructor() {
    this.tasks = [];
  }

  addTask(task) {
    this.tasks.push({ task, completed: false });
  }

  completeTask(index) {
    if (this.tasks[index]) {
      this.tasks[index].completed = true;
    } else {
      console.log("Task not found!");
    }
  }

  listTasks() {
    console.log("Todo List:");
    this.tasks.forEach((item, i) => {
      const status = item.completed ? "Done" : "Not Done";
      console.log(`${i + 1}. ${item.task} - ${status}`);
    });
  }
}

export default TodoList;
