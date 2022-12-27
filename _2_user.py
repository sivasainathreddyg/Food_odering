from _1_admin import *
user_database={}
ordered_item=[]
def user_registration():
    full_name = input("Enter your full name: ")
    phone_number = int(input("Enter your phone number(10 digit): "))
    email = input("Enter your email ID: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")

    user_database["full_name"] = full_name
    user_database["phone_number"] = phone_number
    user_database["email"] = email
    user_database["address"] = address
    user_database["password"] = password
    print("user registration done")
    for i in user_database:
        print(f"{i}:{user_database[i]}")

def user_login():
    if bool(user_database):
        email = input("Enter your email ID to login: ")
        password = input("Enter your password: ")
        if user_database["email"] == email and user_database["password"] == password:
            print("Welcome User")
            user_functions()
        else:
            print("\nPlease check your credentials and try again")
    else:
        print("\nUser need to register first\n")
 
def user_functions():
    while True:
        options=int(input("\n1.Place New Order\n2.Order History\n3.Update Profile\n4.Exit\n:"))
        if options == 1:
            place_new_order()

        elif options == 2:
            order_history()

        elif options == 3:
            update_profile()
            
        elif options == 4: 
            break

        else:
            print("Select valid option")

def place_new_order():
    if len(food)>0:
        print("current menu:")
        menu=[]
        for id in food:
            menu.append([food[id]["Name"],food[id]["Quantity"],food[id]["Price"]])
            for i in range(len(menu)):
                print(f"{i+1}.{menu[i]}")
            while True:
                options=int(input("\n1.Order\n2.Go Back\n:"))
                if options==1:
                    food_order = input("Enter the number of the food you want to order separated by comma: ").split(",")
                    for i in food_order:
                        food_list=int(i)
                        print(food_list)
                        if food_list <= len(menu):
                            ordered_item.append(menu[food_list-1])
                        else:
                            print(f"\nThe opted food item {food_list} is not available")
                    print("\nFollowing is the food items selected : \n")
                    for food_selected in ordered_item:
                      print(food_selected)
                elif options == 2:
                  break
    else:
        print("\nFood menu is currently empty\n")

def order_history():
    if len(ordered_item)>0:
        print("\n list of ordered food so far:\n")
        for items in ordered_item:
            print(items)
        else:
            print("\n No ordered history")

def update_profile():
    for i in user_database:
        print(f"{i}:{user_database}")
    while True:
        options = int(input("\n1.Name\n2.Phone Number\n3.Email ID\n4.Password\n5.Address\n6.GO BACK\n"))
        if options == 1:
            user_database["full_name"] = input("Enter your updated full name: ")
            print("\nName updated successfully\n")
        elif options == 2:
            user_database["phone_number"] = input("Enter your updated phone number: ")
            print("\Phone Number updated successfully\n")
        elif options == 3:
            user_database["email"] = input("Enter your updated email: ")
            print("\nEmail updated successfully\n")

        elif options == 4:
            user_database["password"] = input("Enter your updated password: ")
            print("\Password updated successfully\n")

        elif options == 5:
            user_database["address"] = input("Enter your updated address: ")
            print("\nAddress updated successfully\n")
                
        elif options == 6: 
            break

        else:
            print("\nPlease choose from the available options")
        

        

    
                        




    

