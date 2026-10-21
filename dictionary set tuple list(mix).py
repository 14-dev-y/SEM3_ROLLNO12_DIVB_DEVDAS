# Create a Python program to store information of 3 students using a dictionary.
"""
For every student, store:

Student name
A list of subjects
Subject-wise marks as tuples (subject, marks)

Perform the following operations:

Display the name of every student.
Display all subjects using the stored list.
Calculate the total marks using the tuple data.
Find the highest mark without using max().
Check whether "Python" is present in the subjects.
Display subjects having marks greater than 75.
Create a set of subjects in which the student scored 80 or above.
Find the common high-scoring subjects between Student 1 and Student 2 using set intersection.
Display the final student having the highest total marks.
Add a new subject "AI" with marks 88 for Student 1.

"""

d1 = {
    "S1": {
        "name": "Dev",
        "subjects": ["Python", "DBMS", "OS"],
        "marks": [("Python", 85), ("DBMS", 72), ("OS", 90)]
    },
    "S2": {
        "name": "Pooja",
        "subjects": {"Python", "DBMS", "OS"},
        "marks": [("Python", 82), ("DBMS", 88), ("OS", 70)]
    },
    "S3": {
        "name": "Maahi",
        "subjects": ["Python", "DBMS", "OS"],
        "marks": [("Python", 95), ("DBMS", 91), ("OS", 86)]
    }
}

highest_total = 0
top_student = ""

for key, student in d1.items():

    print("\nStudent:", student["name"])
    print("Subjects:", student["subjects"])

    total = 0
    highest = 0
    high_subjects = set()

    for subject, marks in student["marks"]:
        total = total + marks

        if marks > highest:
            highest = marks

        if marks > 75:
            print(subject, ":", marks)

        if marks >= 80:
            high_subjects.add(subject)

    print("Total:", total)
    print("Highest:", highest)
    print("Python Present:", "Python" in student["subjects"])
    print("80+ Subjects:", high_subjects)

    if total > highest_total:
        highest_total = total
        top_student = student["name"]

# to find out the common 80 plus marks subject between the student 1 and student 2 

print("\nCommon 80+ Subjects:", 
      set([subject for subject, marks in d1["S1"]["marks"] if marks >= 80]) &
      set([subject for subject, marks in d1["S2"]["marks"] if marks >= 80]))

#update the s1 with new sub and marks

d1["S1"]["subjects"].append("AI")
d1["S1"]["marks"].append(("AI", 88))

print("\nUpdated Student 1:")
print(d1["S1"])

# prints the top student and their marks total

print("\nTop Student:", top_student)
print("Highest Total:", highest_total)