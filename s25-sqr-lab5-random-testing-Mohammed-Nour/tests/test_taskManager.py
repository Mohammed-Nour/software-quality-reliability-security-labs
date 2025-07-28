# This is the template for the TaskManager test cases for mutation testing.
# Please add your tests below. 

import pytest
from taskManager.taskManager import TaskManager
from taskManager.task import Task
import os


def test_task_mark_completed():
    task = Task("Task 1", "high", "2025-04-01")
    assert not task.completed  # Initially not completed
    task.mark_completed()
    assert task.completed  # Should be marked as completed


def test_task_to_dict():
    task = Task("Test 2", "medium", "2025-04-01", completed=True)
    task_dict = task.to_dict()
    assert task_dict == {
        "task_text": "Test 2",
        "priority": "medium",
        "due_date": "2025-04-01",
        "completed": True
    }


def test_task_from_dict():
    task_data = {
        "task_text": "Test 3",
        "priority": "low",
        "due_date": "2025-04-01",
        "completed": False
    }
    task = Task.from_dict(task_data)
    assert task.task_text == "Test 3"
    assert task.priority == "low"
    assert task.due_date == "2025-04-01"
    assert not task.completed


def test_add_task():
    manager = TaskManager()
    manager.add_task("Test 4", "high", "2025-04-01")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].task_text == "Test 4"


def test_remove_task():
    manager = TaskManager()
    manager.add_task("Task 5", "low", "2025-04-01")
    manager.add_task("Task 6", "medium", "2025-04-02")
    manager.remove_task(0)
    assert len(manager.tasks) == 1
    assert manager.tasks[0].task_text == "Task 6"


def test_complete_task():
    manager = TaskManager()
    manager.add_task("Test 7", "high", "2025-04-01")
    manager.complete_task(0)
    assert manager.tasks[0].completed


def test_save_and_load_tasks():
    manager = TaskManager()
    manager.add_task("Test 8", "high", "2025-04-01")
    # temp_file = "tasks.json"
    manager.save_tasks()
    manager.remove_task(0)
    manager.load_tasks()
    assert len(manager.tasks) == 1
    assert manager.tasks[0].task_text == "Test 8"