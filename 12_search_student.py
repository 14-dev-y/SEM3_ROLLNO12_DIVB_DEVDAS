"""Program 12: Search for a student name in a file."""

target = input("Enter student name to search: ").strip().casefold()

with open("students.txt", "w", encoding="utf-8") as file:
    file.writelines(["Dev\n", "Tanish\n", "Dhruv\n", "Maahi\n", "Keya\n"])

with open("students.txt", "r", encoding="utf-8") as file:
    names = [line.strip().casefold() for line in file]

if target in names:
    print("Student found.")
else:
    print("Student not found.")
