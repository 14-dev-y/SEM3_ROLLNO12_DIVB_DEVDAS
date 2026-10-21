# Separate odd and even numbers into tuples
numbers = tuple(int(input(f"Enter number {i + 1}: ")) for i in range(10))
even = tuple(number for number in numbers if number % 2 == 0)
odd = tuple(number for number in numbers if number % 2 != 0)
print("Even numbers:", even)
print("Odd numbers:", odd)
