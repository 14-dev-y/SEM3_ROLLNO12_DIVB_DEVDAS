f = open("words.txt", "w")

for i in range(3):
    word = input("Enter a word: ")
    f.write(word + "\n")

f.close()

print("File created successfully")

f = open("words.txt", "r")

data = f.read()

char_count = len(data)
print("Character count:", char_count)

words = data.split()
word_count = len(words)

print("Word count:", word_count)

vowels = "aeiouAEIOU"
vowel_count = 0

for ch in data:
    if ch in vowels:
        vowel_count += 1

print("Vowel count:", vowel_count)

f.close()
