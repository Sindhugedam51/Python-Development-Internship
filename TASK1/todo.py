class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔ Completed" if self.completed else "❌ Pending"
        return f"{self.description} - {status}"


tasks = []


def add_task():
    description = input("Enter task description: ")
    tasks.append(Task(description))
    print("\n✅ Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n===== TO-DO LIST =====")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()


def mark_task_completed():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1].mark_completed()
            print("\n🎉 Task marked as completed!\n")
        else:
            print("\n❌ Invalid task number.\n")

    except ValueError:
        print("\n❌ Please enter a valid number.\n")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted = tasks.pop(task_number - 1)
            print(f"\n🗑 '{deleted.description}' deleted successfully.\n")
        else:
            print("\n❌ Invalid task number.\n")

    except ValueError:
        print("\n❌ Please enter a valid number.\n")


while True:

    print("=" * 35)
    print("      TO-DO LIST APPLICATION")
    print("=" * 35)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        mark_task_completed()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("\nThank you for using To-Do List Application!")
        break

    else:
        print("\n❌ Invalid Choice. Please try again.\n")