
tasks=[]

def create_task(task):
    tasks.append(task)
    print(f"Task {task} created successfully.")

def show():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")