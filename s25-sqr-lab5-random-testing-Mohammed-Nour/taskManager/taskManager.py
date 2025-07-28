import json  
from .task import Task  

class TaskManager:
    def __init__(self):
        self.tasks = []  
        self.load_tasks()

    def add_task(self, task_text, priority, due_date):
        task = Task(task_text, priority, due_date)
        self.tasks.append(task)
        print("Task added successfully!")  # pragma: no mutate

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Removed task: {removed_task.task_text}")  
        else:
            print("Invalid task number!")  

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print("Task marked as completed!")  
        else:
            print("Invalid task number!")  

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")  
        else:
            print("\nTask List:")  
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Not Completed" 
                print(f"{i}. Task: {task.task_text}")  
                print(f"   Priority: {task.priority}")  
                print(f"   Due Date: {task.due_date}")  
                print(f"   Status: {status}\n")  

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file)
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = [Task.from_dict(task_data) for task_data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []  
