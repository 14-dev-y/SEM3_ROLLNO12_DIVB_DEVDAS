s1 = {10, 20, 30, 30, 40}
s2 = {30, 40, 50, 60}

s1.add(50)

s2.update([70, 80])

print("Set 1:", s1)
print("Set 2:", s2)

print("Union:", s1 | s2)

print("Intersection:", s1 & s2)

print("Difference:", s1 - s2)

print("Symmetric Difference:", s1 ^ s2)

print("Subset:", s1.issubset(s2))

print("Superset:", s1.issuperset(s2))

print("Disjoint:", s1.isdisjoint(s2))

s3 = s1.copy()
print("Copy:", s3)

s1.difference_update(s2)
print("After Difference Update:", s1)