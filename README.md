# Todo App

An in-memory Python console todo application that allows you to manage your tasks through a simple command-line interface.

## Features

- Add new tasks
- View all tasks
- Update existing tasks
- Delete tasks
- Mark tasks as complete

## Installation

1. Make sure you have Python 3.13+ installed
2. Install dependencies using UV:
   ```bash
   uv sync
   ```

Or run directly with:
```bash
uv run src/main.py
```

## Usage

Run the application:
```bash
python src/main.py
```

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
Task added: 1. [ ] Buy groceries

> add "Walk the dog"
Task added: 2. [ ] Walk the dog

> view
Your Todo List:
1. [ ] Buy groceries
2. [ ] Walk the dog

> complete 1
Task marked as complete: 1. [x] Buy groceries

> view
Your Todo List:
1. [x] Buy groceries
2. [ ] Walk the dog

> quit
Goodbye!
```

## Project Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── todo.py            # Task and TodoList data models
│   ├── services/
│   │   ├── __init__.py
│   │   └── todo_manager.py    # Todo management service
│   └── cli/
│       ├── __init__.py
│       └── cli_interface.py   # CLI interface and command parsing
├── main.py                   # Application entry point
└── pyproject.toml            # Project dependencies and configuration
```