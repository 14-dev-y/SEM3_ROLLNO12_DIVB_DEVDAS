"""Program 23: Read student names safely and handle a missing file."""

try:
    with open("students.txt", "r", encoding="utf-8") as file:
        names = file.readlines()
except FileNotFoundError:
    print("Student file not found.")
else:
    print("Student names:")
    for name in names:
        print(name.strip())
finally:
    print("Read attempt finished.")
