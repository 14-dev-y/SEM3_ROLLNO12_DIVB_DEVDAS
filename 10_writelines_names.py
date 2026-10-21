"""Program 10: Use writelines() to save multiple names."""

names = ["Dev\n", "Tanish\n", "Dhruv\n", "Maahi\n", "Keya\n"]

with open("names.txt", "w", encoding="utf-8") as file:
    file.writelines(names)

print("Names written successfully.")
