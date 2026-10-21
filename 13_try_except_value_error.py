"""Program 13: Handle invalid integer input with ValueError."""

try:
    age = int(input("Enter your age: "))
    print("Next year you will be", age + 1)
except ValueError:
    print("Invalid input. Please enter a whole number.")
