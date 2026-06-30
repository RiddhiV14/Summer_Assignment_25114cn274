students = []

while True:
    print("\n----- Student Record System -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        students.append([roll, name, marks])
        print("Student Added Successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No Records Found")
        else:
            print("\nRoll\tName\tMarks")
            for student in students:
                print(student[0], "\t", student[1], "\t", student[2])

    elif choice == 3:
        search = input("Enter Roll No to Search: ")
        found = False

        for student in students:
            if student[0] == search:
                print("Record Found")
                print("Roll No:", student[0])
                print("Name:", student[1])
                print("Marks:", student[2])
                found = True
                break

        if not found:
            print("Student Not Found")

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")