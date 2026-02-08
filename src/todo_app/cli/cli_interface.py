"""
CLI interface and command parsing for the todo application
"""
from ..services.todo_manager import TodoManager


class CLIInterface:
    """
    Command-line interface for the todo application
    """

    def __init__(self, todo_manager: TodoManager):
        self.todo_manager = todo_manager

    def display_tasks(self):
        """Display all tasks in a formatted way"""
        tasks = self.todo_manager.get_all_tasks()

        if not tasks:
            print("No tasks in the list.")
            return

        print("\nYour Todo List:")
        for task in tasks:
            print(task)

    def parse_command(self, command_line: str):
        """Parse and execute a command from the command line"""
        # Properly parse quoted strings
        parts = self._parse_arguments(command_line.strip())

        if not parts or not parts[0]:
            print("Error: Please provide a command. Available commands: add, view, update, delete, complete, quit")
            return True  # Continue the main loop

        cmd = parts[0].lower()

        if cmd == 'view':
            self.display_tasks()
        elif cmd == 'add':
            if len(parts) < 2:
                print("Error: Please provide a task description. Usage: add 'task description'")
                return True
            description = parts[1]
            if not description:
                print("Error: Task description cannot be empty")
                return True
            if len(description) > 500:
                print("Error: Task description must not exceed 500 characters")
                return True
            try:
                task = self.todo_manager.add_task(description)
                print(f"Task added: {task}")
            except ValueError as e:
                print(f"Error: {e}")
        elif cmd == 'update':
            if len(parts) < 3:
                print("Error: Please provide task ID and new description. Usage: update <id> 'new description'")
                return True
            try:
                task_id = int(parts[1])
                if task_id <= 0:
                    print("Error: Task ID must be a positive integer")
                    return True
                new_description = parts[2]
                if not new_description:
                    print("Error: Task description cannot be empty")
                    return True
                if len(new_description) > 500:
                    print("Error: Task description must not exceed 500 characters")
                    return True
                task = self.todo_manager.update_task(task_id, new_description)
                print(f"Task updated: {task}")
            except ValueError as e:
                if "invalid literal" in str(e):
                    print("Error: Task ID must be a valid integer")
                else:
                    print(f"Error: {e}")
        elif cmd == 'delete':
            if len(parts) < 2:
                print("Error: Please provide task ID. Usage: delete <id>")
                return True
            try:
                task_id = int(parts[1])
                if task_id <= 0:
                    print("Error: Task ID must be a positive integer")
                    return True
                self.todo_manager.delete_task(task_id)
                print(f"Task {task_id} deleted successfully")
            except ValueError as e:
                if "invalid literal" in str(e):
                    print("Error: Task ID must be a valid integer")
                else:
                    print(f"Error: {e}")
        elif cmd == 'complete':
            if len(parts) < 2:
                print("Error: Please provide task ID. Usage: complete <id>")
                return True
            try:
                task_id = int(parts[1])
                if task_id <= 0:
                    print("Error: Task ID must be a positive integer")
                    return True
                task = self.todo_manager.mark_task_complete(task_id)
                print(f"Task marked as complete: {task}")
            except ValueError as e:
                if "invalid literal" in str(e):
                    print("Error: Task ID must be a valid integer")
                else:
                    print(f"Error: {e}")
        elif cmd in ['quit', 'exit', 'q']:
            return False  # Return False to exit the main loop
        else:
            print(f"Unknown command: '{cmd}'. Available commands: add, view, update, delete, complete, quit")

        return True

    def _parse_arguments(self, command_line: str):
        """Parse command line with proper handling of quoted strings"""
        if not command_line:
            return []

        parts = []
        current_part = ""
        in_quotes = False
        quote_char = None

        i = 0
        while i < len(command_line):
            char = command_line[i]

            if char in ['"', "'"] and not in_quotes:
                in_quotes = True
                quote_char = char
            elif char == quote_char and in_quotes:
                in_quotes = False
                quote_char = None
            elif char == ' ' and not in_quotes:
                if current_part:
                    parts.append(current_part)
                    current_part = ""
            else:
                current_part += char

            i += 1

        # Add the last part if there is one
        if current_part or (len(parts) > 0 and command_line.endswith(' ')):
            parts.append(current_part)

        return parts

    def run(self):
        """Run the main CLI loop"""
        print("Welcome to the Todo App!")
        print("Commands: add 'description', view, quit")

        while True:
            try:
                command = input("\nEnter command: ").strip()

                if command.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break

                should_continue = self.parse_command(command)
                if not should_continue:
                    continue

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break