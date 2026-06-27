employees = []

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")

        employee = {
            "id": emp_id,
            "name": name,
            "department": department
        }

        employees.append(employee)
        print("Employee added successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records")
            for emp in employees:
                print("ID         :", emp["id"])
                print("Name       :", emp["name"])
                print("Department :", emp["department"])

    elif choice == 3:
        search_id = int(input("Enter Employee ID: "))
        found = False

        for emp in employees:
            if emp["id"] == search_id:
                print("\nEmployee Found")
                print("ID         :", emp["id"])
                print("Name       :", emp["name"])
                print("Department :", emp["department"])
                found = True
                break

        if found == False:
            print("Employee not found.")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")