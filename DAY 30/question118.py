books = []

while True:
    print("\n----- Mini Library System -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter Book Name: ")
        books.append(book)
        print("Book Added!")

    elif choice == 2:
        if len(books) == 0:
            print("Library is Empty")
        else:
            print("\nBooks Available:")
            for b in books:
                print(b)

    elif choice == 3:
        search = input("Enter Book Name: ")

        if search in books:
            print("Book Found")
        else:
            print("Book Not Found")

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")