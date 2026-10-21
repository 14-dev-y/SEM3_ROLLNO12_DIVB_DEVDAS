# Input values and print tuple in reverse order
values = input("Enter values separated by commas: ").split(",")
items = tuple(value.strip() for value in values)
print("Original tuple:", items)
print("Reversed tuple:", items[::-1])
