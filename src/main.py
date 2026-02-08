"""
Application entry point for the Todo App
"""
from todo_app.services.todo_manager import TodoManager
from todo_app.cli.cli_interface import CLIInterface


def main():
    """Main entry point for the application"""
    todo_manager = TodoManager()
    cli_interface = CLIInterface(todo_manager)

    cli_interface.run()


if __name__ == "__main__":
    main()