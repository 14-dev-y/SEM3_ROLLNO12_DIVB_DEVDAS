students = []

while True:
    print("\n1 Add  2 Display  3 Search  4 Update  5 Delete")
    print("6 Sort by name  7 Sort by marks  8 Topper  9 Average  0 Exit")
    choice = input("Choose: ")

    if choice == "1":
        roll = input("Roll number: ")
        name = input("Name: ")
        marks = float(input("Marks: "))
        students.append([roll, name, marks])
    elif choice == "2":
        for student in students:
            print(student)
    elif choice == "3":
        roll = input("Roll number to search: ")
        found = False
        for student in students:
            if student[0] == roll:
                print(student)
                found = True
        if not found:
            print("Student not found")
    elif choice == "4":
        roll = input("Roll number to update: ")
        found = False
        for student in students:
            if student[0] == roll:
                student[1] = input("New name: ")
                student[2] = float(input("New marks: "))
                found = True
                break
        if not found:
            print("Student not found")
    elif choice == "5":
        roll = input("Roll number to delete: ")
        for student in students:
            if student[0] == roll:
                students.remove(student)
                print("Student deleted")
                break
        else:
            print("Student not found")
    elif choice == "6":
        students.sort(key=lambda student: student[1].lower())
        print("Sorted by name")
    elif choice == "7":
        students.sort(key=lambda student: student[2], reverse=True)
        print("Sorted by marks")
    elif choice == "8":
        if students:
            print("Topper:", max(students, key=lambda student: student[2]))
        else:
            print("No student records")
    elif choice == "9":
        if students:
            print("Average marks:", sum(student[2] for student in students) / len(students))
        else:
            print("No student records")
    elif choice == "0":
        break
    else:
        print("Invalid choice")
