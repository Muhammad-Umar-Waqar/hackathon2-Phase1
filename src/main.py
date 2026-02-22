"""
Application entry point for the Todo App
"""
import sys
import os

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

from todo_app.services.todo_manager import TodoManager
from todo_app.cli.cli_interface import CLIInterface


def main():
    """Main entry point for the application"""
    todo_manager = TodoManager()
    cli_interface = CLIInterface(todo_manager)

    cli_interface.run()


if __name__ == "__main__":
    main()