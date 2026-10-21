"""Program 06: Use w mode to write and overwrite file content."""

with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("This is the new content.\n")
    file.write("Old content is replaced in w mode.\n")

with open("diary.txt", "r", encoding="utf-8") as file:
    print(file.read())
