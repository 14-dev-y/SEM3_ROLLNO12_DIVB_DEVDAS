"""Program 21: Use raise to reject negative marks."""

try:
    marks = int(input("Enter marks (0-100): "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
except ValueError as error:
    print("Invalid marks:", error)
else:
    print("Marks accepted:", marks)
