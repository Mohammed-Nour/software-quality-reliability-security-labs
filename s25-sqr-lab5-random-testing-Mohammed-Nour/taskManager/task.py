import json  

class Task:
    def __init__(self, task_text, priority, due_date, completed=False):  
        self.task_text = task_text  
        self.priority = priority  
        self.due_date = due_date  
        self.completed = completed  

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "task_text": self.task_text,  
            "priority": self.priority,  
            "due_date": self.due_date,  
            "completed": self.completed
        }

    @staticmethod
    def from_dict(task_data):
        return Task(
            task_data['task_text'],
            task_data['priority'],
            task_data['due_date'],
            task_data['completed']
        )
