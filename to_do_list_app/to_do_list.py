import json
my_tasks: list = []

def add_task(user_input):
    global item_list
    if not my_tasks:
        load_data()
    my_tasks.append({"id": len(my_tasks)+ 1 ,"task": user_input})
    file_add = json.dumps(my_tasks)
    with open("D:\\decocelabs projects\\to_do_list_app\\list.json",'w') as file:
        json.dump(my_tasks,file,indent=4)
    print(f"{user_input}, added successfully!")
def view_list():
    global my_tasks
    print("====All Items====")
    with open("D:\\decocelabs projects\\to_do_list_app\\list.json",'r') as f:
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
