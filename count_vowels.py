# Count vowels using a tuple
text = input("Enter a string: ").lower()
vowels = ("a", "e", "i", "o", "u")
count = 0
for character in text:
    if character in vowels:
        count += 1
print("Total vowels:", count)
