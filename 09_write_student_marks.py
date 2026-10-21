"""Program 09: Take student marks and save them to a file."""

students = {"Dev": 85, "Tanish": 91, "Dhruv": 78, "Maahi": 94, "Keya": 88}

with open("marks.txt", "w", encoding="utf-8") as file:
    for name, marks in students.items():
        file.write(f"{name}: {marks}\n")

print("Marks saved to marks.txt")
