# Find maximum and minimum without max() and min()
numbers = tuple(int(value) for value in input("Enter numbers separated by spaces: ").split())
if numbers:
    largest = smallest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    print("Maximum:", largest)
    print("Minimum:", smallest)
else:
    print("No numbers entered")
