"""
Demo script to showcase the enhanced Todo App UI
"""
import sys
import os

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

from src.todo_app.services.todo_manager import TodoManager
from src.todo_app.cli.cli_interface import CLIInterface

def demo():
    """Run a demo of the enhanced UI"""
    todo_manager = TodoManager()
    cli = CLIInterface(todo_manager)

    # Show welcome
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich import box

    console = Console(force_terminal=True, legacy_windows=False)

    welcome_text = Text()
    welcome_text.append("✨ Welcome to the ", style="bold white")
    welcome_text.append("Todo App", style="bold cyan")
    welcome_text.append(" ✨\n\n", style="bold white")
    welcome_text.append("Manage your tasks efficiently with style!\n", style="dim")
    welcome_text.append("Type ", style="white")
    welcome_text.append("help", style="bold cyan")
    welcome_text.append(" to see available commands.", style="white")

    console.print(Panel(welcome_text, border_style="bright_blue", box=box.DOUBLE))

    # Show help
    console.print("\n[bold cyan]Displaying Help:[/bold cyan]")
    cli._display_help()

    # Add some demo tasks
    console.print("\n[bold cyan]Adding Demo Tasks:[/bold cyan]")
    todo_manager.add_task("Complete project documentation")
    console.print("[green]✅ Task added:[/green] Complete project documentation [dim](ID: 1)[/dim]")

    todo_manager.add_task("Review pull requests")
    console.print("[green]✅ Task added:[/green] Review pull requests [dim](ID: 2)[/dim]")

    todo_manager.add_task("Update dependencies")
    console.print("[green]✅ Task added:[/green] Update dependencies [dim](ID: 3)[/dim]")

    # Mark one as complete
    console.print("\n[bold cyan]Marking Task as Complete:[/bold cyan]")
    todo_manager.mark_task_complete(1)
    console.print("[green]✅ Task marked as complete:[/green] [white]Complete project documentation[/white]")

    # Display all tasks
    console.print("\n[bold cyan]Displaying All Tasks:[/bold cyan]")
    cli.display_tasks()

    # Show goodbye
    console.print("\n")
    goodbye_text = Text("👋 Demo Complete! Run 'python src/main.py' to start using the app!", style="bold green")
    console.print(Panel(goodbye_text, border_style="green"))

if __name__ == "__main__":
    demo()
