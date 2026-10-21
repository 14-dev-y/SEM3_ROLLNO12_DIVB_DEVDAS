students = {}

for i in range(5):
    roll_no = int(input("Enter roll number: "))
    marks = input("Enter 6 comma-separated marks out of 50: ")
    students[roll_no] = [int(mark.strip()) for mark in marks.split(",")]

subject_results = {}

for subject in range(6):
    subject_marks = [marks[subject] for marks in students.values()]
    subject_results[f"Subject {subject + 1}"] = (
        min(subject_marks),
        max(subject_marks)
    )

print("Minimum and maximum marks (min, max):")
print(subject_results)
