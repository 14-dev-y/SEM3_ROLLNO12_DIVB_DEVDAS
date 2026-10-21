numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

print("First five:", numbers[:5])
print("Last five:", numbers[-5:])
print("Alternate:", numbers[::2])
print("Reverse:", numbers[::-1])
