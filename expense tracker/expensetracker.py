total = 0.0
while True:
    print("\n" + "="*20)
    print("   EXPENSE TRACKER")
    print("="*20)
    print("1.Add expenses.")
    print("2.Quit and show total.")
    user = input("Enter you choice: ")
    if user == '1':
        while True:   
            data = input("Enter expense amount (or 'q' to stop): ").lower()
            if data == 'q':
                break
            elif data.strip() == "":
                continue
            else:
                try: 
                    expense = float(data)
                    if expense < 0:
                        print("Expense cannot be negative!")     
                        continue
                    total += expense       
                    print(f"Added {expense} to total.")
                except ValueError:
                    print("Invalid Data! Please enter a number.")
    elif user == '2':
        print(f"\nYour Total expense:{total:.2f}")
        print("Exiting...")
        break
    else:
        print("Invalid Choice! Select 1 or 2.")