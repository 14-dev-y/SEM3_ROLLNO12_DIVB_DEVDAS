from emp import Employee

emp_list = []

while True:
    print("1. Add")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Update")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # ADD
    if choice == 1:

        emp = Employee()

        emp.getData()

        found = False

        for e in emp_list:
            if e.eid == emp.eid:
                found = True
                break

        if found:
            print("Employee with this ID already exists!")

        else:
            emp.calSalary()
            emp_list.append(emp)
            print("Employee added successfully!")

    # DISPLAY
    elif choice == 2:

        if len(emp_list) == 0:
            print("No employees found!")

        else:
            for e in emp_list:
                e.putData()

    # SEARCH
    elif choice == 3:

        eid = int(input("Enter employee ID to search: "))

        found = False

        for e in emp_list:
            if e.eid == eid:
                e.putData()
                found = True
                break

        if not found:
            print("Employee not found!")

    # DELETE
    elif choice == 4:

        eid = int(input("Enter employee ID to delete: "))

        found = False

        for e in emp_list:
            if e.eid == eid:
                emp_list.remove(e)
                found = True
                print("Employee deleted successfully!")
                break

        if not found:
            print("Employee not found!")

    # EXIT
    elif choice == 6:

        print("Exiting...")
        break

    # INVALID
    else:

        print("Invalid choice!")