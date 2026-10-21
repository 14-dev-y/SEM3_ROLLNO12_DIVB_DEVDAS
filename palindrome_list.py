items = input("Enter list items separated by spaces: ").split()

is_palindrome = True
for i in range(len(items) // 2):
    if items[i] != items[len(items) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
