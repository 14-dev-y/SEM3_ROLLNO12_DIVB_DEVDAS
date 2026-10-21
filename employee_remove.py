employees = {
    101: "Dev",
    102: "Tanish",
    103: "Dhruv",
    104: "Maahi",
    105: "Adishree"
}

emp_id = int(input("Enter employee ID to remove: "))

if emp_id in employees:
    del employees[emp_id]
    print("Updated employees:", employees)
else:
    print("Employee ID not found")
