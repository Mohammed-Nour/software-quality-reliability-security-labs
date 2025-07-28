# import json
# from .taskManager import TaskManager
# def main():
#     manager = TaskManager()

#     while True:
#         print("\nCommand Menu:")
#         print("1. Add Task")
#         print("2. Remove Task")
#         print("3. Mark Task as Completed")
#         print("4. List Tasks")
#         print("5. Exit")

#         choice = input("Enter your choice (1/2/3/4/5): ")

#         if choice == "1":
#             task_text = input("Enter task description: ")
#             priority = input("Enter priority (high/medium/low): ")
#             due_date = input("Enter due date (YYYY-MM-DD): ")
#             manager.add_task(task_text, priority, due_date)
#         elif choice == "2":
#             task_index = int(input("Enter the task number to remove: ")) - 1
#             manager.remove_task(task_index)
#         elif choice == "3":
#             task_index = int(input("Enter the task number to mark as completed: ")) - 1
#             manager.complete_task(task_index)
#         elif choice == "4":
#             manager.list_tasks()
#         elif choice == "5":
#             manager.save_tasks()
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")

# if __name__ == "__main__":
#     main()
