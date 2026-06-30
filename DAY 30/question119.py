employees = []

while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        empid = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        employees.append([empid, name, salary])
        print("Employee Added Successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No Employee Records")
        else:
            print("\nID\tName\tSalary")
            for emp in employees:
                print(emp[0], "\t", emp[1], "\t", emp[2])

    elif choice == 3:
        search = input("Enter Employee ID: ")
        found = False

        for emp in employees:
            if emp[0] == search:
                print("Employee Found")
                print("ID:", emp[0])
                print("Name:", emp[1])
                print("Salary:", emp[2])
                found = True
                break

        if not found:
            print("Employee Not Found")

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")