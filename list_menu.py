items = []

while True:
    print("\n1 Append  2 Insert  3 Extend  4 Remove  5 Pop")
    print("6 Sort  7 Reverse  8 Count  9 Index  10 Copy")
    print("11 Clear  12 Display  0 Exit")
    choice = input("Choose: ")

    if choice == "1":
        items.append(input("Value: "))
    elif choice == "2":
        index = int(input("Index: "))
        value = input("Value: ")
        items.insert(index, value)
    elif choice == "3":
        items.extend(input("Values separated by commas: ").split(","))
    elif choice == "4":
        value = input("Value to remove: ")
        if value in items:
            items.remove(value)
        else:
            print("Value not found")
    elif choice == "5":
        if items:
            print("Removed:", items.pop())
        else:
            print("List is empty")
    elif choice == "6":
        items.sort()
    elif choice == "7":
        items.reverse()
    elif choice == "8":
        value = input("Value to count: ")
        print(items.count(value))
    elif choice == "9":
        value = input("Value to find: ")
        if value in items:
            print("Index:", items.index(value))
        else:
            print("Value not found")
    elif choice == "10":
        copied = items.copy()
        print("Copy:", copied)
    elif choice == "11":
        items.clear()
    elif choice == "12":
        print(items)
    elif choice == "0":
        break
    else:
        print("Invalid choice")
