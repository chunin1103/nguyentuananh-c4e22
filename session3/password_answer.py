while True:
    pwd = input("Enter your password: ")
    if len(pwd) < 8:
        print("Not long enough")
    elif pwd.isdigit():
        print("Must not contain only digits")
    elif pwd.isupper() or pwd.islower():
        print("Password must contain both UPPER and lower case")

    else:
        print("OK")
        break