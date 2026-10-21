items = input("Enter items separated by spaces: ").split()
frequency = {}

for item in items:
    frequency[item] = frequency.get(item, 0) + 1

print("Frequency table:", frequency)
