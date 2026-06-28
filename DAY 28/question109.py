library = {}

while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        book = input("Enter book name: ")
        library[book] = "Available"
        print("Book added successfully.")

    elif ch == 2:
        book = input("Enter book name: ")
        if book in library and library[book] == "Available":
            library[book] = "Issued"
            print("Book issued.")
        else:
            print("Book not available.")

    elif ch == 3:
        book = input("Enter book name: ")
        if book in library:
            library[book] = "Available"
            print("Book returned.")
        else:
            print("Book not found.")

    elif ch == 4:
        print("\nLibrary Books")
        for book, status in library.items():
            print(book, "-", status)

    elif ch == 5:
        break

    else:
        print("Invalid choice")