employees = {
    101: "Dev",
    102: "Tanish",
    103: "Dhruv",
    104: "Maahi",
    105: "Adishree"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee found:", employees[emp_id])
else:
    print("Employee not found")
