# Quickstart Guide: Phase I: In-Memory Python Console Todo App

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Install dependencies using UV:
   ```bash
   uv sync
   ```
   or if starting fresh:
   ```bash
   uv pip install -e .
   ```

## Running the Application

1. Execute the main application:
   ```bash
   python src/main.py
   ```

   Or with UV:
   ```bash
   uv run src/main.py
   ```

## Using the Todo App

Once the application starts, you'll see a menu with the following options:

### Available Commands
- `add "task description"` - Add a new task with the specified description
- `view` - Display all tasks with their completion status
- `update <id> "new description"` - Update the description of a task by ID
- `delete <id>` - Remove a task by ID
- `complete <id>` - Mark a task as completed by ID
- `quit` - Exit the application

### Example Usage
```
> add "Buy groceries"
Task added: Buy groceries (ID: 1)

> add "Walk the dog"
Task added: Walk the dog (ID: 2)

> view
1. [ ] Buy groceries
2. [ ] Walk the dog

> complete 1
Task 1 marked as complete

> view
1. [x] Buy groceries
2. [ ] Walk the dog

> quit
```

## Development

The application is organized into the following modules:
- `src/todo_app/models/todo.py` - Task data model
- `src/todo_app/services/todo_manager.py` - Business logic for task management
- `src/todo_app/cli/cli_interface.py` - Command-line interface handling
- `src/main.py` - Application entry point

All data is stored in-memory and will be lost when the application exits.