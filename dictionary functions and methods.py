d1 = {
    "name": "Dev",
    "age": 20,
    "course": "Python"
}

print(d1["name"])
# update and modify

d1["city"] = "Ahmedabad"
d1["age"] = 21

# print key value and item(key and value together)

print(d1.keys())
print(d1.values())
print(d1.items())

# get is used to access the value from the key

print(d1.get("course"))

# get does not give keyerror if there is no value else it give none or the default value we had given to print
print(d1.get("phone", "Not Available"))

# update for multiple entries

d1.update({
    "course": "Python Programming",
    "marks": 90
})

# pop is used to delete

d1.pop("marks")

# in and not to check exsisting and not exsisting

print("city" in d1)
print("phone" not in d1)

# pop item is delete the last inserted key value vriable

print(d1.popitem())

# clear is used to delete all the pairs from the dictionary

d1.clear()

print(d1)