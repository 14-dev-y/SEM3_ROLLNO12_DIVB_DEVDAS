employees = {
    101: "Dev",
    102: "Tanish",
    103: "Dhruv",
    104: "Maahi",
    105: "Adishree"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    employees[emp_id] = input("Enter new employee name: ")
    print("Updated employees:", employees)
else:
    print("Employee ID not found")
