"""Program 08: Demonstrate r+ mode for reading and writing."""

with open("edit.txt", "w", encoding="utf-8") as file:
    file.write("Hello World")

with open("edit.txt", "r+", encoding="utf-8") as file:
    print("Original:", file.read())
    file.seek(0)
    file.write("Python")
    file.seek(0)
    print("Updated:", file.read())
