"""Program 17: Handle IndexError when accessing a missing list item."""

names = ["Dev", "Tanish", "Dhruv"]

try:
    print(names[5])
except IndexError:
    print("That list index does not exist.")
