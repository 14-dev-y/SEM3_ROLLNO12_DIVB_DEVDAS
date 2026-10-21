"""Program 16: Handle FileNotFoundError when opening a missing file."""

try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist. Check its name or path.")
