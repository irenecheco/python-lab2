def insert_task(tasklist, task):
    tasklist.append(task)

def remove_task(tasklist, task):
    tasklist.remove(task)

def show_list(tasklist):
    print(sorted(tasklist))

def close():
    exit(0)

tasklist = []
flag = True
while flag==True:
    print("Select an action: ")
    print("1. Insert a new task; ")
    print("2. Remove a task; ")
    print("3. Show all existing task; ")
    print("4. Close the program. ")
    sel = int(input())
    if(sel == 1):
        print("Insert a new task: ")
        task = input()
        insert_task(tasklist, task)
    elif(sel == 2):
        print("Insert the task you want to remove: ")
        task = input()
        remove_task(tasklist, task)
    elif(sel == 3):
        show_list(tasklist)
    elif(sel == 4):
        flag = False
        close()
    else:
        print("ERROR: Option does not exists. ")


