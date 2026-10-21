"""Program 02: Demonstrate opening a file in read mode."""

# Create a sample file first, then read it.
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python file handling\n")
    file.write("Reading files is easy.\n")

file = open("notes.txt", "r", encoding="utf-8")
print(file.read())
file.close()
