menu=((1,"panner",400),(2,"chicken",600),(3,"dessert",150),(4,"noodles",200 ))

while(True):
    print("------HOTEL MENU------\n1.view menu\n2.Order\n3.Generate Bill\n4.exit\n")
    choice=int(input("enter your choice"))
    match choice:
        case 1:
            print("-------Items are:-----\nitem id  name  price\n----------------------")
            for items in menu:
                print(f"item{items[0]}  {items[1]}  {items[2]}")
        case 2:
            pass
            
        case 3:
            pass 
        case 4:
            print("Thank you and visit again")
        case _:
            print("invalid choice")
