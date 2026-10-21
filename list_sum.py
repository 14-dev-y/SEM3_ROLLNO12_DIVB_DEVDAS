first = [int(x) for x in input("Enter first list numbers: ").split()]
second = [int(x) for x in input("Enter second list numbers: ").split()]

if len(first) == len(second):
    third = [first[i] + second[i] for i in range(len(first))]
    print("Sum list:", third)
else:
    print("Lists must have equal size")
