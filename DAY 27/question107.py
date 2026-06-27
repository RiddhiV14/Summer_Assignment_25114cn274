salary_records = []

while True:
    print("\n===== Salary Management System =====")
    print("1. Add Salary Record")
    print("2. Display Salary Records")
    print("3. Search Salary")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))

        record = {
            "id": emp_id,
            "name": name,
            "salary": salary
        }

        salary_records.append(record)
        print("Salary record added successfully!")

    elif choice == 2:
        if len(salary_records) == 0:
            print("No salary records found.")
        else:
            print("\nSalary Records")
            for emp in salary_records:
                print("--------------------------")
                print("ID     :", emp["id"])
                print("Name   :", emp["name"])
                print("Salary :", emp["salary"])

    elif choice == 3:
        search_id = int(input("Enter Employee ID: "))
        found = False

        for emp in salary_records:
            if emp["id"] == search_id:
                print("\nSalary Record Found")
                print("ID     :", emp["id"])
                print("Name   :", emp["name"])
                print("Salary :", emp["salary"])
                found = True
                break

        if found == False:
            print("Record not found.")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")