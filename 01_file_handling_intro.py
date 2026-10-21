"""Program 01: Write student names to a file and read them back."""

# Reference names: Dev, Tanish, Dhruv, Maahi, Keya
names = ["Dev", "Tanish", "Dhruv", "Maahi", "Keya"]

with open("students.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

with open("students.txt", "r", encoding="utf-8") as file:
    print("Student names:")
    print(file.read(), end="")
