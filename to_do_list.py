import sys
# create an empty list to store the tasks
tasks = []

def main():
    options = {
        '1' : add_task,
        '2' : view_task,
        '3' : remove_task,
        '4' : exit_program,
    }

# create a menu
    while True:
        print(
        f"""
Options:
1. Add task
2. View task
3. Remove task
4. Exit
        """
    )
        choice = input("Choose an option (1, 2, 3, 4): ")
        if choice not in options:
            print("Invalid choice!")
            continue
        options[choice]()
        


# add task
def add_task():
    while True:
        try:
            task = input("Add a task: ").strip()
            if not task:
                print("Task cannot be empty!")
                continue
            tasks.append(task)
            save_tasks()

        except EOFError:
            break


# view task
def view_task():
    if len(tasks) == 0:
        print("Task list is empty!")
    else:
        print("Your listed tasks are: ")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# remove task
def remove_task():
    while True:
        task_to_remove = input("Task to remove: ").strip()
        if task_to_remove not in tasks:
            print("Task in not in list!")
            continue
        else:
            tasks.remove(task_to_remove)
            save_tasks()
            break


# implement exit
def exit_program():
    sys.exit(0)

# save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
    

if __name__ == '__main__':
    load_tasks()
    main()