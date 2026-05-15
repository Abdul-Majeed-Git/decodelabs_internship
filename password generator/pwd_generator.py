import random 
import string
import secrets
def pwd_generator(pwd_length):
    secret = string.ascii_letters + string.digits +string.punctuation
    password_char= []
    for i in range(pwd_length):
        password_char.append(secrets.choice(secret))
    password = "".join(password_char)
    print(f"Password: {password}")
try:
    while True:
        print("---------------------------")
        print("====Password Generator====")
        print("---------------------------")
        print("1. Recommend Strong Password. ")
        print("2. Generate Your Password.")
        print("3. Type 'q' to quit.")
        user = input("Enter Your Choice: ").lower()
        if user == "q":
            break
        elif user == '1':
            print("="*30)
            pwd_generator(20)
            print("="*30)
        elif user == '2':
            password_length = int(input("Enter password lenth: "))
            if password_length <= 64:
                print(f"{"="*10}{"="*password_length}")
                pwd_generator(password_length)
                print(f"{"="*10}{"="*password_length}")
            else:
                print("Maximum Password length allowed is 64!")
        else:
            print("Select valid choice!")
except KeyboardInterrupt:
    print("")