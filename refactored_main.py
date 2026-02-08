"""
Todo Application - Phase I: In-Memory Python Console Todo App

A simple command-line todo application that stores tasks entirely in memory.
Features a numbered menu interface for easy navigation.
"""

from datetime import datetime
from typing import List, Optional


class Task:
    """
    Represents a single todo item in the application

    Attributes:
        id: Unique identifier for the task
        title: Brief description/title of the task
        completed: Status indicating whether the task is completed
        created_at: Timestamp when the task was created
    """

    def __init__(self, task_id: int, title: str, completed: bool = False):
        self.id = task_id
        self.title = title
        self.completed = completed
        self.created_at = datetime.now()

    def __str__(self):
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}. {self.title}"


class TodoApp:
    """
    Main application class that manages all tasks in memory
    """

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str) -> Task:
        """Add a new task with the given title"""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        if len(title) > 500:
            raise ValueError("Task title must not exceed 500 characters")

        task = Task(self.next_id, title.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks in the list"""
        return self.tasks[:]

    def get_task_by_id(self, task_id: int) -> Task:
        """Get a specific task by its ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task with ID {task_id} does not exist")

    def update_task(self, task_id: int, new_title: str) -> Task:
        """Update the title of a task by its ID"""
        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty")

        if len(new_title) > 500:
            raise ValueError("Task title must not exceed 500 characters")

        task = self.get_task_by_id(task_id)
        task.title = new_title.strip()
        return task

    def delete_task(self, task_id: int):
        """Delete a task by its ID"""
        task = self.get_task_by_id(task_id)
        self.tasks.remove(task)

    def mark_task_complete(self, task_id: int) -> Task:
        """Mark a task as completed by its ID"""
        task = self.get_task_by_id(task_id)
        task.completed = True
        return task

    def mark_task_incomplete(self, task_id: int) -> Task:
        """Mark a task as incomplete by its ID"""
        task = self.get_task_by_id(task_id)
        task.completed = False
        return task

    def display_menu(self):
        """Display the main menu"""
        print("\n--- Todo Application ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print("Enter your choice (1-7): ", end="")

    def display_tasks(self):
        """Display all tasks with their status"""
        if not self.tasks:
            print("\nNo tasks in the list.")
            return

        print("\nYour Todo List:")
        print("-" * 40)
        for task in self.tasks:
            print(task)
        print("-" * 40)

    def get_task_input(self, prompt: str) -> str:
        """Get task input with validation"""
        while True:
            value = input(prompt).strip()
            if not value:
                print("Error: Input cannot be empty. Please try again.")
                continue
            if len(value) > 500:
                print("Error: Input exceeds 500 characters. Please try again.")
                continue
            return value

    def get_task_id(self, prompt: str) -> int:
        """Get task ID input with validation"""
        while True:
            try:
                value = input(prompt).strip()
                task_id = int(value)
                if task_id <= 0:
                    print("Error: Task ID must be a positive integer. Please try again.")
                    continue
                return task_id
            except ValueError:
                print("Error: Please enter a valid integer. Please try again.")
                continue

    def handle_add_task(self):
        """Handle adding a new task"""
        try:
            title = self.get_task_input("Enter task title: ")
            task = self.add_task(title)
            print(f"Task added: {task}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_view_tasks(self):
        """Handle viewing all tasks"""
        self.display_tasks()

    def handle_update_task(self):
        """Handle updating a task"""
        if not self.tasks:
            print("\nNo tasks available to update.")
            return

        self.display_tasks()
        try:
            task_id = self.get_task_id("Enter task ID to update: ")
            task = self.get_task_by_id(task_id)

            new_title = self.get_task_input(f"Enter new title for task {task_id} ('{task.title}'): ")
            updated_task = self.update_task(task_id, new_title)
            print(f"Task updated: {updated_task}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_delete_task(self):
        """Handle deleting a task"""
        if not self.tasks:
            print("\nNo tasks available to delete.")
            return

        self.display_tasks()
        try:
            task_id = self.get_task_id("Enter task ID to delete: ")
            task = self.get_task_by_id(task_id)
            print(f"About to delete: {task}")
            confirm = input("Are you sure? (y/N): ").strip().lower()

            if confirm in ['y', 'yes']:
                self.delete_task(task_id)
                print(f"Task {task_id} deleted successfully.")
            else:
                print("Deletion cancelled.")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_mark_complete(self):
        """Handle marking a task as complete"""
        if not self.tasks:
            print("\nNo tasks available to mark as complete.")
            return

        incomplete_tasks = [t for t in self.tasks if not t.completed]
        if not incomplete_tasks:
            print("\nAll tasks are already completed.")
            return

        print("\nIncomplete Tasks:")
        for task in incomplete_tasks:
            print(task)

        try:
            task_id = self.get_task_id("Enter task ID to mark complete: ")
            task = self.get_task_by_id(task_id)
            if task.completed:
                print(f"Task {task_id} is already marked as complete.")
                return

            completed_task = self.mark_task_complete(task_id)
            print(f"Task marked as complete: {completed_task}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_mark_incomplete(self):
        """Handle marking a task as incomplete"""
        if not self.tasks:
            print("\nNo tasks available to mark as incomplete.")
            return

        complete_tasks = [t for t in self.tasks if t.completed]
        if not complete_tasks:
            print("\nNo completed tasks to mark as incomplete.")
            return

        print("\nCompleted Tasks:")
        for task in complete_tasks:
            print(task)

        try:
            task_id = self.get_task_id("Enter task ID to mark incomplete: ")
            task = self.get_task_by_id(task_id)
            if not task.completed:
                print(f"Task {task_id} is already marked as incomplete.")
                return

            incomplete_task = self.mark_task_incomplete(task_id)
            print(f"Task marked as incomplete: {incomplete_task}")
        except ValueError as e:
            print(f"Error: {e}")

    def run(self):
        """Run the main application loop"""
        print("Welcome to the Todo Application!")

        while True:
            try:
                self.display_menu()
                choice = input().strip()

                if choice == '1':
                    self.handle_add_task()
                elif choice == '2':
                    self.handle_view_tasks()
                elif choice == '3':
                    self.handle_update_task()
                elif choice == '4':
                    self.handle_delete_task()
                elif choice == '5':
                    self.handle_mark_complete()
                elif choice == '6':
                    self.handle_mark_incomplete()
                elif choice == '7':
                    print("\nThank you for using the Todo Application. Goodbye!")
                    break
                else:
                    print("\nInvalid choice. Please enter a number between 1 and 7.")

            except KeyboardInterrupt:
                print("\n\nOperation interrupted. Exiting...")
                break
            except EOFError:
                print("\n\nExiting...")
                break


def main():
    """Main entry point for the application"""
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()