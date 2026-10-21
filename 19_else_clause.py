"""Program 19: Use else to run code only when no exception occurs."""

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid integer.")
else:
    print("You entered:", number)
    print("Square:", number ** 2)
