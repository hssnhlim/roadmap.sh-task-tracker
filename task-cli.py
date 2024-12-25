import json
import os
import sys
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def update_task(task_id, description):
    """Update the description of a task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Task not found.")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully.")

def mark_task(task_id, status):
    """Mark a task as in-progress or done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status}.")
            return
    print("Task not found.")

def list_tasks(status=None):
    """List tasks by status."""
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']}")

def main():
    """Main CLI function."""
    args = sys.argv[1:]
    if not args:
        print("Usage: task-cli <command> [arguments]")
        return

    command = args[0]
    if command == "add" and len(args) == 2:
        add_task(args[1])
    elif command == "update" and len(args) == 3:
        update_task(int(args[1]), args[2])
    elif command == "delete" and len(args) == 2:
        delete_task(int(args[1]))
    elif command == "mark-in-progress" and len(args) == 2:
        mark_task(int(args[1]), "in-progress")
    elif command == "mark-done" and len(args) == 2:
        mark_task(int(args[1]), "done")
    elif command == "list" and len(args) <= 2:
        list_tasks(args[1] if len(args) == 2 else None)
    else:
        print("Invalid command or arguments.")

if __name__ == "__main__":
    main()
