"""Program 25: Mini program: save five named students and marks, then read records back."""

# Reference names: Dev, Tanish, Dhruv, Maahi, Keya
students = [
    ("Dev", 85),
    ("Tanish", 91),
    ("Dhruv", 78),
    ("Maahi", 94),
    ("Keya", 88),
]

try:
    with open("student_records.txt", "w", encoding="utf-8") as file:
        for name, marks in students:
            if not 0 <= marks <= 100:
                raise ValueError(f"Invalid marks for {name}")
            file.write(f"{name},{marks}\n")

    with open("student_records.txt", "r", encoding="utf-8") as file:
        print("Student records")
        for line in file:
            name, marks = line.strip().split(",")
            print(f"Name: {name} | Marks: {marks}")
except (OSError, ValueError) as error:
    print("Could not process records:", error)
finally:
    print("Program finished.")
