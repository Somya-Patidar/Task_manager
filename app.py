
tasks=[]

def create_task(task):
    tasks.append(task)
    print(f"Task {task} created successfully.")

def show():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task: {task} deleted successfully.")
        print("Updated task list:")
        show()
