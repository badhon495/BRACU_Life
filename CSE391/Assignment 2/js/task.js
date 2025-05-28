document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('task-input');
    const addTaskButton = document.getElementById('add-task-button');
    const taskList = document.getElementById('task-list');

    // Load tasks from localStorage
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    // Function to save tasks to localStorage
    const saveTasks = () => {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };

    // Function to render tasks
    const renderTasks = () => {
        taskList.innerHTML = '';
        tasks.forEach((task, index) => {
            const taskItem = document.createElement('li');
            taskItem.className = `task-item ${task.completed ? 'completed' : ''}`;
            taskItem.innerHTML = `
                <input type="checkbox" ${task.completed ? 'checked' : ''} data-index="${index}">
                <span>${task.text}</span>
                <button data-index="${index}">Delete</button>
            `;
            taskList.appendChild(taskItem);
        });
    };

    // Function to add a new task
    const addTask = () => {
        const taskText = taskInput.value.trim();
        if (taskText) {
            tasks.push({ text: taskText, completed: false });
            taskInput.value = '';
            saveTasks();
            renderTasks();
        }
    };

    // Function to delete a task
    const deleteTask = (index) => {
        tasks.splice(index, 1);
        saveTasks();
        renderTasks();
    };

    // Function to toggle task completion
    const toggleTaskCompletion = (index) => {
        tasks[index].completed = !tasks[index].completed;
        saveTasks();
        renderTasks();
    };

    // Event listeners
    // add id instead of type
    addTaskButton.addEventListener('click', addTask);
    taskList.addEventListener('click', (e) => {
        if (e.target.tagName === 'BUTTON') {
            deleteTask(e.target.dataset.index);
        } else if (e.target.tagName === 'INPUT') {
            toggleTaskCompletion(e.target.dataset.index);
        }
    });

    // Initial render
    renderTasks();
});
