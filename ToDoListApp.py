# ALL TASKS // HOLY CRAP!!! I'M SCARED!!!!

tasks = []

def user_interface():        
        print("Welcome to the To-Do List App!\n")
        print("Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")

def add_task():
    new_task = input("Input task to add: ").strip().capitalize()
    if new_task not in tasks:
        tasks.append(f"{new_task}: Incomplete")
        print(f"Task has been added: {new_task}")                    
    else:
        print(input("Task already exists. Enter new task."))

def view_tasks():
    print("\nCurrent Tasks: ")
    if not tasks:
        print("No tasks avaialable.")
    else:
        for task in tasks:
            print(task)

def task_complete():
    view_tasks()
    complete_task = input("Choose task to complete: ").strip().capitalize()
    for i, task in enumerate(tasks):
        if task.startswith(complete_task) and 'Complete' not in task:
            tasks[i] = complete_task + ': Complete'
            print(f"{complete_task} has been completed! Great job!")
            return
    print(f"{complete_task} ask does not exist or has already been completed.")
    
def delete_task():
    delete_task = input("Enter task to remove: ").strip().capitalize()
    for task in tasks:
        if task.startswith(delete_task):
            tasks.remove(task)
            print(f"{delete_task} has been removed from list! Keep crushing it!")
            return
    print(f"{delete_task} task does not exist in list.")

def main():

    while True:
        user_interface()

        try:            
            choice = int(input("Please choose option: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Thank you for choosing the 'To-Do List Application'!")
                break
            else:
                print("Invalid choice. Please choose valid option.")
        except ValueError:
            print("Invalid input. Please choose from list of options (1-5)")

        finally:
            print()
            
    
main()