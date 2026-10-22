"""Mini Task Manager - starter version for Git branching practice."""

tasks = []


def show_menu():
    print("\n=== Mini Task Manager ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Exit")


def add_task():
    task = input("Enter task name: ").strip()
    tasks.append({"name": task, "completed": False})
    print("Task added.")


def list_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{number}. [{status}] {task['name']}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
