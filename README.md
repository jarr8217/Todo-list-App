# Todo CLI Application

The Todo CLI Application is a simple command-line interface (CLI) program written in Python. It allows users to manage their to-do tasks efficiently by adding, viewing, and deleting tasks from a list. The app provides a straightforward user experience with a menu-driven interface.

- **Menu Navigation**: A user-friendly interface to select operations.
- **Task Management**: Add, view, and delete tasks dynamically.
- **Validation**: Input validation for task names and menu options.
- **Interactive Features**: Confirmation prompts for critical operations like deletion.

## Features

- Add new tasks to your to-do list.
- View all current tasks with a count of total tasks.
- Delete tasks with confirmation to prevent accidental deletions. The app prompts users to confirm with 'y' or 'n' before removing the selected task.
- Input validation for menu options and task names.
- Runs directly in the terminal or command line.

This project demonstrates best practices in Python programming, including modular function design, validation, and user interaction.

---

## Installation and Running

To set up and run the application locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/todo-cli.git
   cd todo-cli
   ```

2. **Run the Application**
   ```bash
   python todo.py
   ```

3. **Usage**
   - Follow the menu prompts to add, view, or delete tasks.
   - Exit the application using the menu option.

---

## Example Usage

### Adding a Task
```plaintext
Enter the task you want to add (max 50 characters): Buy groceries
Task "Buy groceries" added successfully.
```

### Viewing Tasks
```plaintext
Current to-do tasks (3)
1. Laundry
2. Study
3. Buy groceries
```

### Deleting a Task
```plaintext
Enter the task number you want to delete: 3
Are you sure you want to delete "Buy groceries"? (y/n): y
Task "Buy groceries" deleted successfully.
```

---




