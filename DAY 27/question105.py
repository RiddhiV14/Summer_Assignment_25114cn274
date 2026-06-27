students = []

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }

        students.append(student)
        print("Student record added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nStudent Records")
            for s in students:
                print("Roll Number :", s["roll"])
                print("Name        :", s["name"])
                print("Marks       :", s["marks"])

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")