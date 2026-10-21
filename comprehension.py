numbers = list(range(1, 101))

print("Squares:", [n ** 2 for n in numbers])
print("Cubes:", [n ** 3 for n in numbers])
print("Even:", [n for n in numbers if n % 2 == 0])
print("Odd:", [n for n in numbers if n % 2 != 0])
print("Multiples of 5:", [n for n in numbers if n % 5 == 0])
