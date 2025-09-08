tasks = []

# todoList="/Day1_9_25/todo.txt"
def load_exist_task():
    try:
        with open("Day1_9_25/todo.txt", "r") as file:
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
    tasks.append({"id": gen_TaskId(), "task": task, "task_status": "pending"})
    if tasks:
        save_to_file(tasks)
        print(f'Task: {task} added ✅')
    else:
        print("❌ Task not add to file")
    print("")
    

# function to add tasks to file
def save_to_file(tasks):

    try:
        with open("Day1_9_25/todo.txt", "w") as file:
            for task in tasks:
                file.write(f"{task['id']},{task['task']},{task['task_status']}\n")
    except Exception as e:
        print(e)
# function to delete all tasks at once
def delete_all():
    print("⚠️  Warning! you are about to delete all task")
    choice=input("Do you still want to delete all ? (Y/N)")
    if choice.upper() == "Y":
        if tasks:
            tasks.clear()
            print("All task Deleted ✅")
            save_to_file(tasks)
        else:
            print("❌ There is no task avaliable to delete")
    elif choice.lower() == "N":
        return False
    else:
        print("❌ Invalid input")
        return False
# function to remove task
def removetask(task_id):
    task_to_remove = None
    try:
        task_id = int(task_id)
    except ValueError:
        print(f"❌ Invalid task ID: {task_id}")
        return
    for task in tasks:
        if int(task['id']) == task_id:
            task_to_remove = task
            break
    if task_to_remove:
        print("")
        tasks.remove(task_to_remove)
        print(f"Task: {task_to_remove['task']} removed ✅")
        save_to_file(tasks)
    else:
        print("")
        print(f"❌ Task with Id: {task_id} not found")

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
        print("❌ You do not have any task available")
# function for update task staus
def update_status(task_id):
    try:
        task_id=int(task_id)
    except ValueError:
        print(f"❌ Invalid task ID: {task_id}")
        return
    for task in tasks:
        if int(task["id"])==task_id:
            task['task_status']="Completed"
            print(f"Task with Task ID: {task_id} updated sucessfully ✅")
    save_to_file(tasks)
# main function
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
    print("4. Update task status")
    print("5. Delete all tasks")
    print("6. Exit")
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
        task_id = input("View your todo list and enter the Id of the task you want to update: ")
        update_status(task_id)
    elif choice == "5":
        delete_all()
    elif choice == "6":
        break
    else:
        print("❌ Invalid choice selected")
print("")
print("==============================================================")
print("============= Thanks for using Olasquare program =============")
print("==============================================================")
print()