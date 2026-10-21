#dynamic matrix

rows=int(input("enter number of rows "))
cols=int(input("enter number of column "))

print("enter element of matrix A ")
A=[]
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input("enter value ")))
    A.append(row)
for i in A:
    for j in i: 
        print(j,end=" ")
    print("")

# Input second matrix
print("Enter elements of Matrix B:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input("enter value ")))
    B.append(row)


# Matrix Addition
print("\nMatrix Addition:")
addition = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    addition.append(row)

for row in addition:
    print(row)
