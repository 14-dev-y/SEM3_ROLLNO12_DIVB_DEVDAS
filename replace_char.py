# Replace every o with @ without using replace()
text = input("Enter a string: ")
result = ""
for character in text:
    if character == "o":
        result += "@"
    else:
        result += character
print(result)
