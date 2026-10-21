numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
k = int(input("Enter rotation amount: "))

if numbers:
    k = k % len(numbers)
    left = numbers[k:] + numbers[:k]
    right = numbers[-k:] + numbers[:-k] if k else numbers[:]
    print("Left rotation:", left)
    print("Right rotation:", right)
else:
    print("List is empty")
