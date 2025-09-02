# Simple To-Do List Application

# List to store tasks
tasks = [
#     {
#         'id':1,
#         'task_name':"food eating",
#         'status':"inprogress"
#     }
]

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added!')

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print("Task not found!")

# Function to display all tasks
def view_tasks():
    if tasks:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):  # Start numbering from 1
            print(f'{idx}. {task}')
    else:
        print("No tasks in your list!")
#function to update
def update_task_status(id):
    for task in tasks:
        if task['id']==id:
            task['status']='Completed'
            print("Task updated")
        else:
            print("Task not Found")

# Infinite loop to keep the program running until user exits
while True:
    print("\nOperations you can Perform:\n 1. Add Task\n 2. Remove Task\n 3. View Tasks\n 4. Update Tasks\n 5. Exit\n")

    # Ask user for their choice
    choice = input("Enter your choice: ")

    if choice == '1':
        id=1
        task_name = input("Enter task: ")
        new_task= [{'id':id,
        'task_name':task_name,
        'status':"inprogress"}]
        add_task(new_task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        id= input("Enter the task id: ")
        update_task_status(id)
    elif choice == '5':
        print ("==========================================================")
        print ("======== Exiting program. Have a productive day! =========")
        print ("==========================================================")
        print("")
        break
    else:
        print("Invalid choice! Please select a valid option.")