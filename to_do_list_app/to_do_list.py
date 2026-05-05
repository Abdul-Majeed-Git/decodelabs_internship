import json
my_tasks: list = []

def add_task(user_input):
    global item_list
    my_tasks.append({"id": len(my_tasks)+ 1 ,"task": user_input})
    file_add = json.dumps(my_tasks)
    with open("list.json",'w') as file:
        json.dump(my_tasks,file,indent=4)

def view_list():
    global my_tasks
    with open("list.json",'r') as f:
        my_tasks = json.load(f)
        for i,j in enumerate(my_tasks):
            print(i+1,".",j['task'])


if __name__ == "__main__":
    while True:
        print("----Menu----")
        print("1.Add Item")
        print("2.View items")
        print("3.Exit")
        
        user_input = input("Enter your choice:")
        if user_input == '1':
            user_in = input("Add item: ")
            add_task(user_in)
        elif user_input == '2':
            view_list()
        elif user_input == '3':
            break
        else:
            print("Wrong choice")
