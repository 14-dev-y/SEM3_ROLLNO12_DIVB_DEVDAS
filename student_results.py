students = {
    1: [80, 75, 90, 85, 88],
    2: [70, 82, 78, 80, 76],
    3: [95, 91, 89, 94, 96]
}

results = {}

for roll_no, marks in students.items():
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"
    results[roll_no] = (total, percentage, grade)

print(results)
