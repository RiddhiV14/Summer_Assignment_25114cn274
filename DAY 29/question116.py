inventory = {}

while True:
    print("\n1. Add Item")
    print("2. Update Quantity")
    print("3. Delete Item")
    print("4. Display Inventory")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        inventory[item] = qty
        print("Item added.")

    elif ch == 2:
        item = input("Enter item name: ")
        if item in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[item] = qty
            print("Quantity updated.")
        else:
            print("Item not found.")

    elif ch == 3:
        item = input("Enter item name: ")
        if item in inventory:
            del inventory[item]
            print("Item deleted.")
        else:
            print("Item not found.")

    elif ch == 4:
        print("\nInventory")
        for item, qty in inventory.items():
            print(item, "-", qty)

    elif ch == 5:
        break

    else:
        print("Invalid choice.")