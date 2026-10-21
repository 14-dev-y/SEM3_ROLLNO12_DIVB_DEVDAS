"""Program 20: Use finally to close a file whether an error occurs or not."""

file = None
try:
    file = open("cleanup.txt", "w", encoding="utf-8")
    file.write("File cleanup demonstration.")
    print("Data written.")
except OSError as error:
    print("File error:", error)
finally:
    if file is not None and not file.closed:
        file.close()
    print("Finally block executed.")
