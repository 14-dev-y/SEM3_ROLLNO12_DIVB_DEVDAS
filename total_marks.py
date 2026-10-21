# Total marks with and without sum()
t2 = (85, 90, 78, 88, 92)

total = 0
for mark in t2:
    total += mark
print("Total without sum():", total)
print("Total with sum():", sum(t2))
