import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks, description):
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{i+1}. {task['description']} [{status}]")

def mark_task_completed(tasks, task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = True
        save_tasks(tasks)
        print(f"Task {task_id+1} marked as completed")
    else:
        print("Invalid task number")

def delete_task(tasks, task_id):
    if 0 <= task_id < len(tasks):
        task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f"Deleted task: {task['description']}")
    else:
        print("Invalid task number")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            task_id = int(input("Enter task number to complete: ")) - 1
            mark_task_completed(tasks, task_id)
        elif choice == "4":
            task_id = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, task_id)
        elif choice == "5":
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()

