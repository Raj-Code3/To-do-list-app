# To-Do List App
TASK_FILE = "tasks.txt"

def read_tasks():

    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        return [task.strip() for task in tasks]

    except FileNotFoundError:
        return []


def save_tasks(tasks):

    with open(TASK_FILE, "w") as file:

        for task in tasks:
            file.write(task + "\n")


def add_task():

    task = input("Enter new task: ")

    tasks = read_tasks()

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks():

    tasks = read_tasks()

    if len(tasks) == 0:
        print("No tasks found!")
        return

    print("\nYour Tasks:")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")



def delete_task():

    tasks = read_tasks()

    if len(tasks) == 0:
        print("No tasks to delete!")
        return

    view_tasks()

    num = int(input("Enter task number to delete: "))

    if num < 1 or num > len(tasks):
        print("Invalid task number!")
        return

    removed = tasks.pop(num - 1)

    save_tasks(tasks)

    print(f"Task '{removed}' deleted successfully!")
    

def update_task():

    tasks = read_tasks()

    if len(tasks) == 0:
        print("No tasks to update!")
        return

    view_tasks()

    num = int(input("Enter task number to update: "))

    if num < 1 or num > len(tasks):
        print("Invalid task number!")
        return

    new_task = input("Enter new task: ")

    tasks[num - 1] = new_task

    save_tasks(tasks)

    print("Task updated successfully!")



while True:

    print("\n===== TO-DO LIST APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        update_task()

    elif choice == "5":
        print("Exiting App...")
        break

    else:
        print("Invalid Choice!")