"""
TodoManager service to manage tasks in the todo application
"""
from typing import List
from ..models.todo import TodoList, Task


class TodoManager:
    """
    Service to manage todos with all required operations
    """

    def __init__(self):
        self.todo_list = TodoList()

    def add_task(self, title: str) -> Task:
        """Add a new task with the given title"""
        return self.todo_list.add_task(title)

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return self.todo_list.get_all_tasks()

    def update_task(self, task_id: int, new_title: str) -> Task:
        """Update the title of a task by its ID"""
        return self.todo_list.update_task(task_id, new_title)

    def delete_task(self, task_id: int):
        """Delete a task by its ID"""
        return self.todo_list.delete_task(task_id)

    def mark_task_complete(self, task_id: int) -> Task:
        """Mark a task as completed by its ID"""
        return self.todo_list.mark_task_complete(task_id)

    def mark_task_pending(self, task_id: int) -> Task:
        """Mark a task as pending by its ID"""
        return self.todo_list.mark_task_pending(task_id)

    def get_task_by_id(self, task_id: int) -> Task:
        """Get a specific task by its ID"""
        return self.todo_list.get_task_by_id(task_id)