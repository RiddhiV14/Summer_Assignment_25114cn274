tickets = 5

while True:
    print("\n1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Check Available Tickets")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        n = int(input("How many tickets? "))
        if n <= tickets:
            tickets -= n
            print("Ticket booked successfully.")
        else:
            print("Not enough tickets available.")

    elif ch == 2:
        n = int(input("How many tickets to cancel? "))
        tickets += n
        print("Ticket cancelled.")

    elif ch == 3:
        print("Available Tickets =", tickets)

    elif ch == 4:
        break

    else:
        print("Invalid choice")