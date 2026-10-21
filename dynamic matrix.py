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

