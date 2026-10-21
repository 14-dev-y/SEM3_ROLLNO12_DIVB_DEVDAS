"""Program 14: Catch ZeroDivisionError while dividing numbers."""

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter valid numbers.")
