"""Program 22: Read marks from a file and calculate the average."""

marks = [85, 91, 78, 94, 88]

with open("marks.txt", "w", encoding="utf-8") as file:
    for mark in marks:
        file.write(str(mark) + "\n")

with open("marks.txt", "r", encoding="utf-8") as file:
    saved_marks = [int(line.strip()) for line in file if line.strip()]

average = sum(saved_marks) / len(saved_marks) if saved_marks else 0
print("Marks:", saved_marks)
print("Average:", average)
