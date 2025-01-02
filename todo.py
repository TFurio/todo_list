import os

# Initialize an empty list to store tasks
todo_list = []

def display_menu():
    print("\n=== Todo List Menu ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not todo_list:
        print("No tasks in the list!")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(todo_list, 1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['task']} [{status}]")

def mark_task_completed():
    view_tasks()
    if not todo_list:
        return

    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

