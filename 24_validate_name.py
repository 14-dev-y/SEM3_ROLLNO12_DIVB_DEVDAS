"""Program 24: Raise an exception if a student name is blank."""

try:
    name = input("Enter student name: ").strip()
    if not name:
        raise ValueError("Name cannot be blank.")
except ValueError as error:
    print("Invalid name:", error)
else:
    print("Welcome,", name.title())
