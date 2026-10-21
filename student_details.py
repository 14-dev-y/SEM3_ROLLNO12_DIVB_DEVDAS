students = {}

for i in range(5):
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    degree = input("Enter degree: ")
    subject = input("Enter favourite subject: ")
    initial = name[0].upper()
    students[initial] = [age, degree, subject]

print(students)
# If two students have the same initial, the later entry replaces the earlier one.
