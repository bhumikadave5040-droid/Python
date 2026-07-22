

grocery = {
    "Spices": {"Turmeric":20, "Chilli Powder":40, "pav bhaji masala":50},
    "Dry Fruits": {"Almonds":100, "Cashew":150, "Raisins":80},
    "Snacks": {"Chips":20, "Biscuits":30, "Namkeen":25}
}

while True:

    print("\n1. View Items")
    print("2. Buy Item")
    print("3. Generate Bill")
    print("4. Exit")

    ch = int(input("Enter Choice: "))

    match ch:

        case 1:
            print("\nAvailable Items:")
            for i, items in grocery.items():
                print(i, ":", items)

        case 2:
            cat=input("Enter Category: ")
            for cat in grocery:
                if cat in grocery:
                    item=input("Enter Item: ")
                    if item in grocery[cat]:
                        quantity=int(input("Enter Quantity: "))
                        price=grocery[cat][item]*quantity
                        print(f"Price for {quantity} {item}(s): {price}")
                    else:
                        print("Item not found in category.")
                else:
                    print("Category not found.")

        case 4:
            print("Thank You!")
            break

       
        case 3:
            pass
        case _:
            print("Invalid Choice")