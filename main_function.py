from _1_admin import *
from _2_user import *
print("---------------welcome to food app application---------")
while True:
    options=int(input("\n1.admin_registration\n2.admin_login\n3.admin_functions\n4.user_registration\n5.user_login\n6.user_functions\n7.place_new_order\n8.order_history\n9.update_profile\n10.exit\n"))
    if options==1:
      admin_registration()
    elif options==2:
      admin_login()
    elif options==3:
      admin_functions()
    elif options==4:
        user_registration()
    elif options==5:
        user_login()
    elif options==6:
        user_functions()
    elif options==7:
        place_new_order()
    elif options==8:
        order_history()
    elif options==9:
        update_profile()
    elif options==10:
        break
    else:
        print("enter a valid options")



