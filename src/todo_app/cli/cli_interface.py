"""
CLI interface and command parsing for the todo application
"""
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
from ..services.todo_manager import TodoManager


class CLIInterface:
    """
    Command-line interface for the todo application
    """

    def __init__(self, todo_manager: TodoManager):
        self.todo_manager = todo_manager
        # Configure console with proper encoding for Windows
        self.console = Console(force_terminal=True, legacy_windows=False)

    def display_tasks(self):
        """Display all tasks in a formatted way"""
        tasks = self.todo_manager.get_all_tasks()

        if not tasks:
            self.console.print(Panel(
                "[yellow]No tasks in the list. Add one with:[/yellow] [cyan]add 'your task'[/cyan]",
                title="📋 Todo List",
                border_style="blue"
            ))
            return

        table = Table(
            title="📋 Your Todo List",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta",
            border_style="blue"
        )

        table.add_column("ID", style="cyan", justify="center", width=6)
        table.add_column("Status", justify="center", width=10)
        table.add_column("Task", style="white")
        table.add_column("Created", style="dim", width=19)

        for task in tasks:
            status = "✅ Done" if task.completed else "⏳ Pending"
            status_style = "green" if task.completed else "yellow"
            created_time = task.created_at.strftime("%Y-%m-%d %H:%M:%S")

            table.add_row(
                str(task.id),
                f"[{status_style}]{status}[/{status_style}]",
                task.title,
                created_time
            )

        self.console.print(table)

    def parse_command(self, command_line: str):
        """Parse and execute a command from the command line"""
        # Properly parse quoted strings
        parts = self._parse_arguments(command_line.strip())

        if not parts or not parts[0]:
            self.console.print("[red]❌ Error:[/red] Please provide a command. Type [cyan]help[/cyan] for available commands.")
            return True  # Continue the main loop

        cmd = parts[0].lower()

        if cmd == 'help':
            self._display_help()
        elif cmd == 'view':
            self.display_tasks()
        elif cmd == 'add':
            if len(parts) < 2:
                self.console.print("[red]❌ Error:[/red] Please provide a task description.\n[dim]Usage:[/dim] [cyan]add 'task description'[/cyan]")
                return True
            description = parts[1]
            if not description:
                self.console.print("[red]❌ Error:[/red] Task description cannot be empty")
                return True
            if len(description) > 500:
                self.console.print("[red]❌ Error:[/red] Task description must not exceed 500 characters")
                return True
            try:
                task = self.todo_manager.add_task(description)
                self.console.print(f"[green]✅ Task added:[/green] [white]{task.title}[/white] [dim](ID: {task.id})[/dim]")
            except ValueError as e:
                self.console.print(f"[red]❌ Error:[/red] {e}")
        elif cmd == 'update':
            if len(parts) < 3:
                self.console.print("[red]❌ Error:[/red] Please provide task ID and new description.\n[dim]Usage:[/dim] [cyan]update <id> 'new description'[/cyan]")
                return True
            try:
                task_id = int(parts[1])
                if task_id <= 0:
                    self.console.print("[red]❌ Error:[/red] Task ID must be a positive integer")
                    return True
                new_description = parts[2]
                if not new_description:
                    self.console.print("[red]❌ Error:[/red] Task description cannot be empty")
                    return True
                if len(new_description) > 500:
                    self.console.print("[red]❌ Error:[/red] Task description must not exceed 500 characters")
                    return True
                task = self.todo_manager.update_task(task_id, new_description)
                self.console.print(f"[green]✅ Task updated:[/green] [white]{task.title}[/white] [dim](ID: {task.id})[/dim]")
            except ValueError as e:
                if "invalid literal" in str(e):
                    self.console.print("[red]❌ Error:[/red] Task ID must be a valid integer")
                else:
                    self.console.print(f"[red]❌ Error:[/red] {e}")
        elif cmd == 'delete':
            if len(parts) < 2:
                self.console.print("[red]❌ Error:[/red] Please provide task ID.\n[dim]Usage:[/dim] [cyan]delete <id>[/cyan]")
                return True
            try:
                task_id = int(parts[1])
                if task_id <= 0:
                    self.console.print("[red]❌ Error:[/red] Task ID must be a positive integer")
                    return True
                self.todo_manager.delete_task(task_id)
                self.console.print(f"[green]✅ Task {task_id} deleted successfully[/green]")
            except ValueError as e:
                if "invalid literal" in str(e):
                    self.console.print("[red]❌ Error:[/red] Task ID must be a valid integer")
                else:
                    self.console.print(f"[red]❌ Error:[/red] {e}")
        elif cmd == 'complete':
            if len(parts) < 2:
                self.console.print("[red]❌ Error:[/red] Please provide task ID.\n[dim]Usage:[/dim] [cyan]complete <id>[/cyan]")
                return True
            try:
                task_id = int(parts[1])
                if task_id <= 0:
                    self.console.print("[red]❌ Error:[/red] Task ID must be a positive integer")
                    return True
                task = self.todo_manager.mark_task_complete(task_id)
                self.console.print(f"[green]✅ Task marked as complete:[/green] [white]{task.title}[/white]")
            except ValueError as e:
                if "invalid literal" in str(e):
                    self.console.print("[red]❌ Error:[/red] Task ID must be a valid integer")
                else:
                    self.console.print(f"[red]❌ Error:[/red] {e}")
        elif cmd == 'pending':
            if len(parts) < 2:
                self.console.print("[red]❌ Error:[/red] Please provide task ID.\n[dim]Usage:[/dim] [cyan]pending <id>[/cyan]")
                return True
            try:
                task_id = int(parts[1])
                if task_id <= 0:
                    self.console.print("[red]❌ Error:[/red] Task ID must be a positive integer")
                    return True
                task = self.todo_manager.mark_task_pending(task_id)
                self.console.print(f"[yellow]⏳ Task marked as pending:[/yellow] [white]{task.title}[/white]")
            except ValueError as e:
                if "invalid literal" in str(e):
                    self.console.print("[red]❌ Error:[/red] Task ID must be a valid integer")
                else:
                    self.console.print(f"[red]❌ Error:[/red] {e}")
        elif cmd in ['quit', 'exit', 'q']:
            return False  # Return False to exit the main loop
        else:
            self.console.print(f"[red]❌ Unknown command:[/red] '{cmd}'. Type [cyan]help[/cyan] for available commands.")

        return True

    def _display_help(self):
        """Display help information with all available commands"""
        help_table = Table(
            title="📚 Available Commands",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold cyan",
            border_style="blue"
        )

        help_table.add_column("Command", style="cyan", width=20)
        help_table.add_column("Description", style="white")
        help_table.add_column("Example", style="yellow")

        help_table.add_row("help", "Show this help message", "help")
        help_table.add_row("view", "Display all tasks", "view")
        help_table.add_row("add 'task'", "Add a new task", "add 'Buy groceries'")
        help_table.add_row("update <id> 'text'", "Update a task", "update 1 'Buy milk'")
        help_table.add_row("complete <id>", "Mark task as complete", "complete 1")
        help_table.add_row("pending <id>", "Mark task as pending", "pending 1")
        help_table.add_row("delete <id>", "Delete a task", "delete 1")
        help_table.add_row("quit / exit / q", "Exit the application", "quit")

        self.console.print(help_table)

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
        # Display welcome banner
        welcome_text = Text()
        welcome_text.append("✨ Welcome to the ", style="bold white")
        welcome_text.append("Todo App", style="bold cyan")
        welcome_text.append(" ✨\n\n", style="bold white")
        welcome_text.append("Manage your tasks efficiently with style!\n", style="dim")
        welcome_text.append("Type ", style="white")
        welcome_text.append("help", style="bold cyan")
        welcome_text.append(" to see available commands.", style="white")

        self.console.print(Panel(
            welcome_text,
            border_style="bright_blue",
            box=box.DOUBLE
        ))

        while True:
            try:
                command = self.console.input("\n[bold cyan]➜[/bold cyan] [white]Enter command:[/white] ").strip()

                if command.lower() in ['quit', 'exit', 'q']:
                    goodbye_text = Text("👋 Goodbye! Have a productive day!", style="bold green")
                    self.console.print(Panel(goodbye_text, border_style="green"))
                    break

                should_continue = self.parse_command(command)
                if not should_continue:
                    continue

            except KeyboardInterrupt:
                self.console.print("\n[yellow]⚠ Interrupted[/yellow]")
                goodbye_text = Text("👋 Goodbye! Have a productive day!", style="bold green")
                self.console.print(Panel(goodbye_text, border_style="green"))
                break
            except EOFError:
                self.console.print("\n[yellow]⚠ EOF detected[/yellow]")
                goodbye_text = Text("👋 Goodbye! Have a productive day!", style="bold green")
                self.console.print(Panel(goodbye_text, border_style="green"))
                break