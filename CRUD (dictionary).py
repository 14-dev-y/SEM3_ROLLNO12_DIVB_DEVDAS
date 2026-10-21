dd = {
    "name": "Dev",
    "age": 20,
    "city": "Ahmedabad"
}

print("Original:", dd)

print("Name:", dd["name"])

dd["age"] = 21
print("After Update:", dd)

dd["marks"] = 85
print("After Adding:", dd)

dd.pop("city")
print("After Delete:", dd)