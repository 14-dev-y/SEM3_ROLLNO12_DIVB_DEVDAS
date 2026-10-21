numbers=[1,2,3,3,4,5,2,6,1,7]
unique=[]
for n in numbers:
    if numbers.count(n)>=1 and n not in unique: unique.append(n)
duplicates=sorted(set(filter(lambda n:numbers.count(n)>1,numbers)))
print("Original:",numbers); print("Without duplicates:",unique); print("Duplicate values:",duplicates)
