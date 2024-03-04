tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def delete_task(task):
    for t in tasks:
        if t["task"] == task:
            tasks.remove(t)
            print(f"Task '{task}' deleted successfully!")
            return
    print(f"Task '{task}' not found!")

def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Complete" if task["completed"] else "Incomplete"
            print(f"{index}. {task['task']} - {status}")

def mark_complete(task):
    for t in tasks:
        if t["task"] == task:
            t["completed"] = True
            print(f"Task '{task}' marked as complete!")
            return
    print(f"Task '{task}' not found!")

def main():
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Complete")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to delete: ")
            delete_task(task)
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            task = input("Enter the task to mark as complete: ")
            mark_complete(task)
        elif choice == "5":
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if _name_ == "_main_":
    main()
