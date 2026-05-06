total = 0
while True:
    print("----Menu----")
    print("1.Add expenses.")
    print("2.Quit(total)")
    user = input("Enter you choice: ")
    if user == '1':
        while True:   
            data = input("Enter 'q' to stop or press enter your expanses to continue: ").lower()
            if data == 'q':
                break
            else:        
                try: 
                    expense = int(data)     
                    total += expense       
                    print(f"Added {expense} to total.")
                except ValueError:
                    print("Invalid Data!!")
    elif user == '2':
        print(f"Your Total expense:{total}")
        print("Exiting...")
        break
    else:
        print("Invalid Choice!")