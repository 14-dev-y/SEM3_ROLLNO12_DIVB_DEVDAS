cities = []

while True:
    print("\n1 Create  2 Read  3 Update  4 Delete  0 Exit")
    choice = input("Choose: ")

    if choice == "1":
        cities.append(input("Enter city: "))
    elif choice == "2":
        print("Cities:", cities)
    elif choice == "3":
        old = input("City to update: ")
        if old in cities:
            index = cities.index(old)
            cities[index] = input("New city name: ")
        else:
            print("City not found")
    elif choice == "4":
        city = input("City to delete: ")
        if city in cities:
            cities.remove(city)
        else:
            print("City not found")
    elif choice == "0":
        break
    else:
        print("Invalid choice")
