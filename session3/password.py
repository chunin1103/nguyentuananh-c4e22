user_name = input("Enter your user name :): ")
while True:
    password = input("Enter your password: ") 
    if len(password) < 8:
        print("Password must contain more than 8 letters ")
        if password.isupper() == True or password.islower() == True:
            print("Account must contain upper and lower")

            
        else:
            break
        

    else:
        print("account ready")
        break
    