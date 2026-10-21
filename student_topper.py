students = [
    [1, "Dev", 85],
    [2, "Tanish", 92],
    [3, "Dhruv", 78],
    [4, "Maahi", 88],
    [5, "Adishree", 95]
]

topper = students[0]
for student in students:
    if student[2] > topper[2]:
        topper = student

print("Topper:", topper)
students.sort(key=lambda student: student[2])
print("Sorted by marks:")
for student in students:
    print(student)
