"""
Create a nested dictionary to store information of 4 students.

For every student, store:

name
age
course
marks
city

Perform the following operations:

Display the name of every student.
Display the course of every student.
Display students whose marks are greater than 75.
Find the student with the highest marks without using max().
Find the average marks of all students.
Check whether a student named "Dev" exists in the dictionary.
Add a new student with complete details.
Modify the marks of an existing student.
Add "semester": 3 inside every student's inner dictionary.
Delete one student's "city" using pop().
Display all student IDs and their details using items().
"""


d1 = {
    "S1": {
        "name": "Dev",
        "age": 20,
        "course": "BCA",
        "marks": 85,
        "city": "Ahmedabad"
    },
    "S2": {
        "name": "Rahul",
        "age": 21,
        "course": "BCA",
        "marks": 72,
        "city": "Mumbai"
    },
    "S3": {
        "name": "Aman",
        "age": 20,
        "course": "BCA",
        "marks": 91,
        "city": "Delhi"
    },
    "S4": {
        "name": "Riya",
        "age": 21,
        "course": "BCA",
        "marks": 68,
        "city": "Pune"
    }
}

for key, student in d1.items():
    print("Name:", student["name"])

for key, student in d1.items():
    print(student["name"], "Course:", student["course"])

print("Students above 75:")

for key, student in d1.items():
    if student["marks"] > 75:
        print(student["name"], student["marks"])

highest = 0
highest_student = ""

for key, student in d1.items():
    if student["marks"] > highest:
        highest = student["marks"]
        highest_student = student["name"]

print("Highest Student:", highest_student)
print("Highest Marks:", highest)

total = 0

for key, student in d1.items():
    total = total + student["marks"]

average = total / len(d1)

print("Average Marks:", average)

print("Dev Exists:", "Dev" in [student["name"] for student in d1.values()])

d1["S5"] = {
    "name": "Karan",
    "age": 20,
    "course": "BCA",
    "marks": 79,
    "city": "Surat"
}

d1["S2"]["marks"] = 80

for key, student in d1.items():
    student["semester"] = 3

d1["S1"].pop("city")

for key, value in d1.items():
    print(key, value)