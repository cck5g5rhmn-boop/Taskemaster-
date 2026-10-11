tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def show_tasks():
    for task in tasks:
        print(task)

add_task("Complete homework")
add_task("Study Python")
show_tasks()
