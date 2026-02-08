"""
Todo model representing a single task in the application
"""
from datetime import datetime
from typing import List


class Task:
    """
    Represents a single todo item in the application

    Attributes:
        id: Unique identifier for the task (auto-incremented)
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
        status = "x" if self.completed else " "
        return f"{self.id}. [{status}] {self.title}"


class TodoList:
    """
    Container for managing multiple tasks

    Attributes:
        tasks: List of Task objects
        next_id: Counter for assigning next available ID
    """

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str) -> Task:
        """Add a new task with the given title"""
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

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

    def mark_task_pending(self, task_id: int) -> Task:
        """Mark a task as pending by its ID"""
        task = self.get_task_by_id(task_id)
        task.completed = False
        return task