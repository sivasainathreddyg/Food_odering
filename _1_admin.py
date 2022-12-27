print("------welcome to food odering------ ")
food={}
FoodId=len(food)+1
admin_database={}
def admin_registration():
    email=input("enter the email to register as admin:")
    password=input("enter the password to register as admin:")

    admin_database['email']=email
    admin_database['password']=password

    print("Register sucessfull")

def admin_login():
    if bool(admin_database):
        print("login as admin")
        email=input("enter the email to login as adimin:")
        password=input("enter the password to login as admin")
        if admin_database['email']==email and admin_database['password']==password:
            print("login sucessfull")
        else:
            print("entered details are went wrong")
    else:
        print("Registerd as admin")
def admin_functions():
    while True:
        options=int(input("\n1.Add Food Items\n2.Edit Food Items\n3.View Food Items\n4.Remove Food Items \n5.Exit\n:"))
        if options==1:
            add_food_items()
        elif options==2:
            edit_food_items()
        elif options==3:
            view_food_items()
        elif options==4:
            remove_food_item()
        elif options==5:
            break
        else:
            print("select from the available option")

def add_food_items():
    try:
        name = input("\nEnter the name of the food to add: ")
        quantity = float(input("Enter the quantity value: "))
        price = float(input("Enter the price in INR: "))
        discount = float(input("How much discount: "))
        stock = float(input("Stock left: "))
        food_list={"Name":name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}
        food[FoodId]=food_list
        print("\nFood items been added successfully")
    except ValueError:
        print("\ncheck your inputs correctly")

def edit_food_items():
    try:
        FoodId=len(food)+1
        while FoodId>1:
            id=int(input("Enter the foodid you want to update the food:"))
            if id in food.keys():
                value=int(input("\nWhat would you like to update: \n1.Food Name\n2.Quantity\n3.Price\n4.Discount\n5.Stock\n6.exit: \n"))
                if value==1:
                    food[id]["Name"] = input("Update the food name: ")
                    print("Food Name updated successfully")
                elif value==2:
                    food[id]["Quantity"] = input("Update the food quantity: ")
                    print("Food quantity updated successfully")
            
                elif value==3:
                    food[id]["Price"] = float(input("update food's price: "))
                    print("Food Price updated successfully")
                    
                elif value==4:
                    food[id]["Discount"] = float(input("Update food's discount: "))
                    print("Food Discount value updated successfully")
                    
                elif value==5:
                    food[id]["Stock"] = float(input("Update food's stock value: "))
                    print("Food Stock value updated successfully")
                    
                elif value==6:
                    break
                else:
                    print("select from the available options")
                    break
            else:
                print(f"\n{id} Id doesn't exit")
                break
        else:
             print("\nCurrently the food items is empty. Add items first then try again.")
    except ValueError:
        print("Enter the valid input")


def view_food_items():
    print("------------food items---------")
    if len(food)>0:
        for id in food:
            print(f"food id:{id}")
            for items in food[id]:
                print(f"{items}:{food[id][items]}")
            print()
            break
        else:
            print("\n food items is currently empty")

def remove_food_item():
    id=int(input("enter a ID to remove food items:"))
    if id in food:
        food.pop(id)
        print(f"\n food items id:{id} deleted ")
    else:
        print(f"\n foodid:{id} doesn't exist")









            