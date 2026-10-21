print("Enter 2x2 matrix A:")
a = []
for i in range(2):
    a.append([int(x) for x in input("Row values: ").split()])

print("Enter 2x2 matrix B:")
b = []
for i in range(2):
    b.append([int(x) for x in input("Row values: ").split()])

addition = [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]
transpose = [[a[j][i] for j in range(2)] for i in range(2)]
row_sums = [sum(row) for row in a]
column_sums = [sum(a[i][j] for i in range(2)) for j in range(2)]

print("Addition:", addition)
print("Transpose of A:", transpose)
print("Row sums of A:", row_sums)
print("Column sums of A:", column_sums)
