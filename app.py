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

