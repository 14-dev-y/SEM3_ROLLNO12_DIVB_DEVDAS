numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
numbers = [0 if number < 0 else number for number in numbers]
print(numbers)
