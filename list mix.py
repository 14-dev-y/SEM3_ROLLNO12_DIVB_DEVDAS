"""
Create a Python program to store the marks of 10 students in a list.

Perform the following operations:

Display all marks.
Calculate the total marks without using sum().
Find the highest mark without using max().
Find the lowest mark without using min().
Display all marks greater than 75.
Create a new list containing only even marks.
Count how many students scored below 40.
Check whether 90 is present in the list.
Remove the last mark from the list.
Add a new mark 85 to the list.
"""

l1 = [85, 72, 91, 38, 67, 90, 55, 76, 34, 82]

print("Marks:", l1)

total = 0

for mark in l1:
    total = total + mark

print("Total:", total)

highest = l1[0]

for mark in l1:
    if mark > highest:
        highest = mark

print("Highest:", highest)

lowest = l1[0]

for mark in l1:
    if mark < lowest:
        lowest = mark

print("Lowest:", lowest)

print("Marks greater than 75:")

for mark in l1:
    if mark > 75:
        print(mark)

even = []

for mark in l1:
    if mark % 2 == 0:
        even.append(mark)

print("Even Marks:", even)

count = 0

for mark in l1:
    if mark < 40:
        count = count + 1

print("Students below 40:", count)

print("90 Present:", 90 in l1)

l1.pop()

l1.append(85)

print("Final List:", l1)