# This project shows Shopping Cart

cart = []

print("─────────|Welcome to the Shopping Cart|─────────")
print("                 ❀ MENU ❀")
print("─────────────────────────────────────────────────")
print("1) Add an items to the Cart")
print("2) Remove an items from the Cart")
print("3) Display the items in Cart")

choice = int(input("See the Menu and type 1,2 and 3 according to your choice: "))

while True:

    if choice == 1:
        cart.append(input("Enter an item to add: "))

        print("─────────|Welcome to the Shopping Cart|─────────")
        print("                 ❀ MENU ❀")
        print("─────────────────────────────────────────────────")
        print("1) Add an items to the Cart")
        print("2) Remove an items from the Cart")
        print("3) Display the items in Cart")

        choice = int(input("See the Menu and type 1,2 and 3 according to your choice: "))

    elif choice == 2:
        cart.remove(input("Enter an item to remove: "))


        print("─────────|Welcome to the Shopping Cart|─────────")
        print("                 ❀ MENU ❀")
        print("─────────────────────────────────────────────────")
        print("1) Add an items to the Cart")
        print("2) Remove an items from the Cart")
        print("3) Display the items in Cart")

        choice = int(input("See the Menu and type 1,2 and 3 according to your choice: "))


    elif choice == 3:
        print(cart)
        break

    else :
        print("Invalid Choice")




