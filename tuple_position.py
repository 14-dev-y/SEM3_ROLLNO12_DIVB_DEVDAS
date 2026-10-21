# Search for an element in nested tuple t4
t4 = ("Dev", ("coding", "music"), ("Tanish", "Dhruv", "Maahi", "Adishree"), "MSc IT")
item = input("Enter an element to search: ").strip()
found = False
for position, element in enumerate(t4):
    if element == item:
        print("Position:", position)
        found = True
    elif isinstance(element, tuple):
        for sub_position, sub_element in enumerate(element):
            if sub_element.strip() == item:
                print("Position:", (position, sub_position))
                found = True
if not found:
    print("Not found")
