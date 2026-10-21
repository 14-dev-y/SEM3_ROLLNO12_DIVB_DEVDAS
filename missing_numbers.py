numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]

if numbers:
    missing = [number for number in range(min(numbers), max(numbers) + 1) if number not in numbers]
    print("Missing numbers:", missing)
else:
    print("No numbers entered")
