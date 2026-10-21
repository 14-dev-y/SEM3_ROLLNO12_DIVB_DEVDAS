# Reverse each string in a tuple
st = ("Pen", "Marker", "Pencil", "Eraser", "Scale")
result = tuple(word[::-1] for word in st)
print(result)
