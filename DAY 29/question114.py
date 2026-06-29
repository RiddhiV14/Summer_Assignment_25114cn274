arr = []

while True:
    print("\n1. Insert Element")
    print("2. Delete Element")
    print("3. Search Element")
    print("4. Display Array")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        n = int(input("Enter element: "))
        arr.append(n)
        print("Element inserted.")

    elif ch == 2:
        n = int(input("Enter element to delete: "))
        if n in arr:
            arr.remove(n)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif ch == 3:
        n = int(input("Enter element to search: "))
        if n in arr:
            print("Element found.")
        else:
            print("Element not found.")

    elif ch == 4:
        print("Array =", arr)

    elif ch == 5:
        break

    else:
        print("Invalid choice.")