# Create nested tuple using user input
name = input("Enter your name: ").strip()
hobbies = tuple(input("Enter your hobbies separated by commas: ").split(","))
friends = tuple(input("Enter friends' names separated by commas (Dev, Tanish, Dhruv, Maahi, Adishree): ").split(","))
degree = input("Enter your degree: ").strip()
t4 = (name, hobbies, friends, degree)
print("Profile tuple:", t4)
