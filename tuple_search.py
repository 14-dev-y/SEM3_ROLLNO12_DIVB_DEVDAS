# Search for a number in nested tuple t3
t1 = ("Dev", "Manoj", "Das")
t2 = (85, 90, 78, 88, 92)
t3 = (t1, t2)
number = int(input("Enter a number to search: "))
if number in t3 or number in t2:
    print("Number found")
else:
    print("Number not found")
