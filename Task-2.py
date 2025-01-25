def add_task(no_task,task):
    no_task.append(task)
    return no_task

    

def view_tasks(no_task):
    if not no_task:
        print("No Tasks found.")
    else:
        print("To-Do List:")
        for i,task in enumerate(no_task):
            print(f"{i+1}.{task}")


def remove_task(no_task,index):
    try:
        del no_task[index-1]
        print("Task removed successfully.")
    except IndexError:
        print("Invalid index")
    return no_task

if __name__ == "__main__" :
    no_task=[]

    while True:
        print("\nTo-Do List Application")
        print("1.Add Task")
        print("2.View Task")
        print("3.Remove Task")
        print("4.Exit")
        choice = input("Enter your choice:")

        if choice=='1':
            task =input("Enter task:")
            no_task =add_task (no_task,task)
            
        elif choice=='2':
            view_tasks(no_task)
        elif choice=='3':
            view_tasks(no_task)
            if no_task:
                index = int(input("Enter task index to remove:"))
                no_task = remove_task( no_task,index)
        elif choice =='4' :
            print("Exiting...")
            break
        else:
            print("Invalid choice.") 
    

