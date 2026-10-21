numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

positive = [number for number in numbers if number > 0]
negative = [number for number in numbers if number < 0]
zero = [number for number in numbers if number == 0]

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
