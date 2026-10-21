# Find each city name length with and without len()
cities = ("Ahmedabad", "Surat", "Vadodara", "Rajkot")
for city in cities:
    count = 0
    for character in city:
        count += 1
    print(city, "length without len():", count, "length with len():", len(city))
