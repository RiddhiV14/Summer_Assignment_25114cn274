balance = 0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        amt = float(input("Enter amount: "))
        balance += amt
        print("Amount deposited.")

    elif ch == 2:
        amt = float(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    elif ch == 3:
        print("Current Balance =", balance)

    elif ch == 4:
        break

    else:
        print("Invalid choice")