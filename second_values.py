numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

if len(unique) < 2:
    print("Need at least two different values")
else:
    largest = smallest = unique[0]
    second_largest = second_smallest = None

    for number in unique[1:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number != largest and (second_largest is None or number > second_largest):
            second_largest = number

        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number != smallest and (second_smallest is None or number < second_smallest):
            second_smallest = number

    print("Second largest:", second_largest)
    print("Second smallest:", second_smallest)
