"""Program 07: Use append mode to add a new student name."""

with open("students.txt", "w", encoding="utf-8") as file:
    file.write("Dev\nTanish\n")

with open("students.txt", "a", encoding="utf-8") as file:
    file.write("Dhruv\n")
    file.write("Maahi\n")
    file.write("Keya\n")

with open("students.txt", "r", encoding="utf-8") as file:
    print(file.read())
