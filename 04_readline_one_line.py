"""Program 04: Use readline() to read one line at a time."""

with open("class.txt", "w", encoding="utf-8") as file:
    file.write("Dev\nTanish\nDhruv\nMaahi\nKeya\n")

with open("class.txt", "r", encoding="utf-8") as file:
    print("First line:", file.readline().strip())
    print("Second line:", file.readline().strip())
