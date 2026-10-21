"""Program 11: Count the number of lines in a file."""

with open("students.txt", "w", encoding="utf-8") as file:
    file.writelines(["Dev\n", "Tanish\n", "Dhruv\n", "Maahi\n", "Keya\n"])

with open("students.txt", "r", encoding="utf-8") as file:
    line_count = len(file.readlines())

print("Total lines:", line_count)
