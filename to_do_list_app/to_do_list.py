import json
my_tasks: list = []

def add_task(user_input):
    global item_list
    my_tasks.append({"id": len(my_tasks)+ 1 ,"task": user_input})

    with open("list.json",'w') as file:
        json.dump(my_tasks,file,indent=4)
    print(f"{user_input}, added successfully!")
def view_list():
    global my_tasks
    print("====All Items====")
    with open("list.json",'r') as f:
        my_tasks = json.load(f)
        for i,j in enumerate(my_tasks):
            print(i+1,".",j['task'])
def load_data():
    global my_tasks
    try:
        with open("list.json",'r') as file:
            my_tasks = json.load(file)
    except:
        my_tasks= []
def delete_item():
    global my_tasks
    if not my_tasks:
        print("List is empty.")
        return
    print("====Delete Item====")
    for i,j in enumerate(my_tasks):
        print(f"{i+1}. {j['task']}")
    print("===================")
    try:
        choice = int(input("Enter number you want to delete item: "))
        if 1<= choice <= len(my_tasks):
            removed_task = my_tasks.pop(choice - 1)
            for index, task in enumerate(my_tasks):
                task['id'] = index + 1
            with open("list.json",'w') as file:
                json.dump(my_tasks,file, indent=4)
            print(f" '{removed_task['task']}' successfully deleted")
        else:
            print("Invalid ID number")
    except ValueError:
        print("Invalid input! Enter number only")
if __name__ == "__main__":
    load_data()
    try:    
        while True:
            print("----Menu----")
            print("1.Add Item")
            print("2.View items")
            print("3.Delete Item")
            print("4.Exit")
            
            user_input = input("Enter your choice:").strip()
            if user_input == '1':
                user_in = input("Add item: ")
                add_task(user_in)
            elif user_input == '2':
                view_list()
            elif user_input == '3':
                delete_item()
            elif user_input == '4':
                break
            else:
                print("Wrong choice")
    except KeyboardInterrupt:
        print("")
