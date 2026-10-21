students = {
    1: [80, 75, 90, 85, 88],
    2: [70, 82, 78, 80, 76],
    3: [95, 91, 89, 94, 96]
}

top_roll_no = max(students, key=lambda roll_no: sum(students[roll_no]))
print("Highest marks roll number:", top_roll_no)
print("Total marks:", sum(students[top_roll_no]))
