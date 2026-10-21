marks = [int(x) for x in input("Enter marks separated by spaces: ").split()]

grades = [
    "A" if mark >= 90 else
    "B" if mark >= 80 else
    "C" if mark >= 70 else
    "D" if mark >= 60 else
    "F"
    for mark in marks
]

print("Grades:", grades)
