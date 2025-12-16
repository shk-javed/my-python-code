import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    """Load tasks from file"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks):
    """Add a new task"""
    task = input("Enter task description: ")
    priority = input("Priority (High/Medium/Low): ").capitalize()
    due_date = input("Due date (DD-MM-YYYY): ")
    
    tasks.append({
        'task': task,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    })
    save_tasks(tasks)
    print("✅ Task added!")

def view_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("No tasks! 🎉")
        return
    
    print("\n" + "="*50)
    print("TO-DO LIST")
    print("="*50)
    
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['completed'] else "✗"
        print(f"{i}. [{status}] {task['task']}")
        print(f"   Priority: {task['priority']} | Due: {task['due_date']}")
        print()

def mark_completed(tasks):
    """Mark task as completed"""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to mark completed: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]['completed'] = True
                save_tasks(tasks)
                print("✅ Task marked as completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

tasks = load_tasks()

while True:
    print("\n" + "="*30)
    print("TO-DO LIST MANAGER")
    print("="*30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("\nEnter choice (1-5): ")
    
    if choice == '1':
        add_task(tasks)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        mark_completed(tasks)
    elif choice == '4':
        # You can implement delete functionality
        print("Delete feature - Try implementing this yourself!")
    elif choice == '5':
        print("Goodbye! Your tasks are saved.")
        break
    else:
        print("Invalid choice!")