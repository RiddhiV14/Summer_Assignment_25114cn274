contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif ch == 2:
        name = input("Enter name: ")
        if name in contacts:
            print("Phone Number =", contacts[name])
        else:
            print("Contact not found.")

    elif ch == 3:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif ch == 4:
        print("\nContact List")
        for name, phone in contacts.items():
            print(name, "-", phone)

    elif ch == 5:
        break

    else:
        print("Invalid choice")