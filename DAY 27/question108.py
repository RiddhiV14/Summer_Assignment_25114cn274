while True:
    print("\n===== Marksheet Generation System =====")
    print(" Generate Marksheet")
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    m1 = float(input("Enter marks of Subject 1: "))
    m2 = float(input("Enter marks of Subject 2: "))
    m3 = float(input("Enter marks of Subject 3: "))
    m4 = float(input("Enter marks of Subject 4: "))
    m5 = float(input("Enter marks of Subject 5: "))

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5
    if percentage >= 90:
            grade = "A+"
    elif percentage >= 80:
            grade = "A"
    elif percentage >= 70:
            grade = "B"
    elif percentage >= 60:
            grade = "C"
    elif percentage >= 40:
            grade = "D"
    else:
            grade = "F"

    if percentage >= 40:
            result = "PASS"
    else:
            result = "FAIL"

    print("\n========== MARKSHEET ==========")
    print("Roll Number :", roll)
    print("Name        :", name)
    print("Total Marks :", total)
    print("Percentage  :", percentage)
    print("Grade       :", grade)
    print("Result      :", result)


   

   
       