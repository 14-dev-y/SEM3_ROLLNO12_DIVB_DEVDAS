# Create a tuple of Gujarat cities from user input
cities = []
count = int(input("How many cities do you want to enter? "))
for i in range(count):
    city = input("Enter city name: ").strip()
    cities.append(city)
cities = tuple(cities)
print("Cities tuple:", cities)
