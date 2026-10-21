# Search for a fruit in a tuple
fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")
fruit = input("Enter a fruit name: ").strip().title()
if fruit in fruits:
    print(fruit, "is available")
else:
    print(fruit, "is not found")
