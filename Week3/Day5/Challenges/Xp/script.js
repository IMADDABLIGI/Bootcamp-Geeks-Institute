// Create an empty array to store tasks
const tasks = [];

// Get DOM elements
const taskForm = document.getElementById('taskForm');
const taskInput = document.getElementById('taskInput');
const listTasks = document.querySelector('.listTasks');
const clearBtn = document.querySelector('.clear-btn');

// Function to add a new task
function addTask() {
    const taskText = taskInput.value.trim();
    
    // Check that the input is not empty
    if (taskText === '') {
        alert('Please enter a task!');
        return;
    }
    
    // Add task to the array
    tasks.push({
        id: Date.now(),
        text: taskText,
        completed: false
    });
    
    // Add task to the DOM
    renderTasks();
    
    // Clear the input field
    taskInput.value = '';
}

// Function to render all tasks in the DOM
function renderTasks() {
    listTasks.innerHTML = '';
    
    tasks.forEach(task => {
        const taskItem = document.createElement('div');
        taskItem.className = 'task-item';
        
        taskItem.innerHTML = `
            <button class="delete-btn" onclick="deleteTask(${task.id})">
                <i class="fas fa-times"></i>
            </button>
            <input type="checkbox" class="task-checkbox" 
                   ${task.completed ? 'checked' : ''} 
                   onchange="toggleTask(${task.id})">
            <label class="task-label ${task.completed ? 'completed' : ''}">${task.text}</label>
        `;
        
        listTasks.appendChild(taskItem);
    });
}

// Function to delete a task
function deleteTask(taskId) {
    const taskIndex = tasks.findIndex(task => task.id === taskId);
    if (taskIndex > -1) {
        tasks.splice(taskIndex, 1);
        renderTasks();
    }
}

// Function to toggle task completion
function toggleTask(taskId) {
    const task = tasks.find(task => task.id === taskId);
    if (task) {
        task.completed = !task.completed;
        renderTasks();
    }
}

// Function to clear all tasks
function clearAllTasks() {
    tasks.length = 0;
    renderTasks();
}

// Event listeners
taskForm.addEventListener('submit', function(e) {
    e.preventDefault();
    addTask();
});

clearBtn.addEventListener('click', clearAllTasks);

// Allow adding tasks by pressing Enter
taskInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        addTask();
    }
});