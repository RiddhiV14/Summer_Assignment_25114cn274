s = input("Enter a string: ")

while True:
    print("\n1. Length")
    print("2. Uppercase")
    print("3. Lowercase")
    print("4. Reverse")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("Length =", len(s))

    elif ch == 2:
        print("Uppercase =", s.upper())

    elif ch == 3:
        print("Lowercase =", s.lower())

    elif ch == 4:
        print("Reverse =", s[::-1])

    elif ch == 5:
        break

    else:
        print("Invalid choice.")