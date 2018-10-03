items = ["T-shirt", "Sweater"]
loop_counter = 0


while True:
    if loop_counter == 0:
        n = str(input("Welcome to our shop, what do you want? \n Please enter C, R, U, D or exit: "))
        loop_counter += 1
    else:    
        n = str(input("What else do you want? \n Please enter C, R, U, D or exit: "))

    if n.upper() == "R":
        print("Our items:", end = " ") 
        print(*items, sep = ", ")

    elif n.upper() == "C":
        while True:
            c_new_item = (input("Enter new item: "))

            if c_new_item.isdigit():
                print("New item cannot be a number")
            elif c_new_item.isupper() or c_new_item.islower():
                print("new item must contain both Lower and UPPER case")
        
            else:
                items.append(c_new_item)
                break
        print("Our items:", end = " ") 
        print(*items, sep = ", ")


    elif n.upper() == "U":

        while True:
            u_position = (input("Update position? "))
            if u_position.isalpha():
                print("Position must be a number")
            elif int(u_position) > len(items):
                print("Location unavailable")
            else:
                break

        
        while True:
            u_item = str(input("Insert new item? "))
            
            if u_item.isdigit():
                print("New item cannot be a number")
            elif u_item.isupper() or u_item.islower():
                print("new item must contain both Lower and UPPER case")
        
            else:
                items.insert((int(u_position) - 1), u_item)
                break

        print("Our items: ", end = "")
        print(*items, sep = ", ")

    elif n.upper() == "D":
        while True:
            d_position = (input("Delete position "))
            if d_position.isalpha():
                print("Delete position must be a number")
            else:
                items.pop(int(d_position) - 1)
                break
        
        print("Our items: ", end = "")
        print(*items, sep = ", ")

    elif n.lower() == "exit":
        break