"""Program 03: Use read() to display the complete file."""

with open("message.txt", "w", encoding="utf-8") as file:
    file.write("Hello Dev!\nWelcome to Python file handling.")

with open("message.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
