"""Program 18: Use multiple except clauses for different exceptions."""

try:
    numbers = [10, 20, 30]
    index = int(input("Enter an index (0-2): "))
    divisor = int(input("Enter a divisor: "))
    print("Answer:", numbers[index] / divisor)
except ValueError:
    print("Enter integers only.")
except IndexError:
    print("Index out of range. Choose 0, 1, or 2.")
except ZeroDivisionError:
    print("Divisor cannot be zero.")
