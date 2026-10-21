def unique_values(values):
    result=[]
    for value in values:
        if value not in result: result.append(value)
    return result
sample=[1,2,3,3,3,3,4,5]
print("Original:",sample); print("Unique:",unique_values(sample))
