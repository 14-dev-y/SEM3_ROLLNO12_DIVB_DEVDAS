"""Program 05: Use readlines() to get all lines as a list."""

with open("class.txt", "w", encoding="utf-8") as file:
    file.writelines(["Dev\n", "Tanish\n", "Dhruv\n", "Maahi\n", "Keya\n"])

with open("class.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
