tasks = []
def load_exist_task():
    try:
        with open("todo.txt", "r") as file:
            for line in file:
                id,task,task_status= line.strip().split(",")
                tasks.append({"id":id,"task":task,"task_status":task_status})
    except ValueError as e:
        print(e)
            
def gen_TaskId():
    import random
    while True:
        rand_id = random.randint(1, 99999)
        if not check_id_exist(rand_id):
            return rand_id
def check_id_exist(id):
    for task in tasks:
        if task["id"] == id:
            return True
# add task function
def addtask(task):
    tasks.append({"id": gen_TaskId(), "task": task, "task_status": False})
    if tasks:
        save_to_file(tasks)
    else:
        print("Task not add to file")
    print("")
    print(f'Task: {task} added')

# function to add tasks to file
def save_to_file(tasks):
    if tasks:
        try:
            with open("todo.txt", "a") as file:
                for task in tasks:
                    file.write(f"{task['id']},{task['task']},{task['task_status']}\n")
        except Exception as e:
            print(e)

def removetask(task_id):
    task_to_remove = None
    try:
        task_id = int(task_id)
    except ValueError:
        print(f"Invalid task ID: {task_id}")
        return
    for task in tasks:
        if task['id'] == task_id:
            task_to_remove = task
            break
    if task_to_remove:
        print("")
        tasks.remove(task_to_remove)
        print(f"Task: {task_to_remove['task']} removed")
    else:
        print("")
        print(f"Task with Id: {task_id} not found")

# funtion view task
def view_task ():
    print("")
    # Filter out tasks with empty or placeholder values
    filtered_tasks = [task for task in tasks if task["task"].strip() != ""]
    if filtered_tasks:
        print("Your task(s)")
        print(
            f"""__________________________________________
| Id |\ttask|\tstatus  |
------------------------------------------""")                 
        for task in filtered_tasks:
            print(f'{task["id"]}|\t{task["task"]}\t{task["task_status"]}')
    else:
        print("You do not have any task available")

def main():
    load_exist_task()
    print("")
    print("=======================================================")
    print("======== Welcome to Olasquare Todo List App ===========")
    print("=======================================================")
    while True:
        print("")
        print("Select operation to perform")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View task")
        print("4. Exit")
        print("++++++++++++++++++++++++++++")
        print("")
        choice = input("Enter your choice: ")
        # Checking the choice
        if choice == "1":
            task = input("Enter your todo task: ")
            addtask(task)
        elif choice == "2":
            task_id = input("Please view your todo list above and enter the Id of the task you want to delete: ")
            removetask(task_id)
        elif choice == "3":
            view_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice selected")
    print("")
    print("==============================================================")
    print("============= Thanks for using Olasquare program =============")
    print("==============================================================")
    print()
    # tasks= load_exist_task()
    # tasks
main()