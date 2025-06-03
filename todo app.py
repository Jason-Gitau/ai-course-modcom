# define adding a new task

# a list of tasks
tasks=[]

# adding a task
def add_task(name):
    completed=False
    task={
        "name":name,
        "completed":completed
    }
    tasks.append(task)
    return name


def view_task():
    task_num=1
    for task in tasks:
        print(f"{[task_num]}{task['name']} (Completed: {task['completed']})")
        task_num+=1


def status_task():
    while True:
        try:
            task_num_str = input("Enter the number of the task to mark as completed (or 'stop' to go back): ")
            if task_num_str.lower() == 'stop':
                break 

            task_num = int(task_num_str)
            

            
            if 1 <= task_num <= len(tasks):
                
                tasks[task_num - 1]['completed'] = True
                print(f"Task '{tasks[task_num - 1]['name']}' marked as completed!")
                break

            else:
                print("Invalid task number. Please enter a number from the list.")

        except ValueError:
            print("Invalid input. Please enter a number or 'stop'.")

        



def main():
    print("\n menu")
    print()
    print("Type 1 to add a task")
    print("Type 2 to view tasks")
    print("Type 3 to update the status of the task")
    print("Type 4 to exit")
    
    while True:
        menu=input("> ")
        if menu is not "1" or "2" or "3" or "4":
            print("kindly enter a valid input")


        if menu =="4":
            print("see you another day")
            break
        
        elif menu == "1":
            while True:
                user_input=input("input the name of the task: ")
                

                if user_input=="break":
                    break
                else:
                    add_task(user_input)

        elif menu=="2":
            view_task()

        elif menu=="3":
            status_task()

    
        
main()
    


