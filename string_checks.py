words = input("Enter words separated by spaces: ").split()

if words:
    print("Longest:", max(words, key=len))
    print("Shortest:", min(words, key=len))
    vowels = "aeiouAEIOU"
    print("Starting with vowel:", [word for word in words if word and word[0] in vowels])
    print("Ending with consonant:", [
        word for word in words
        if word and word[-1].isalpha() and word[-1] not in vowels
    ])
else:
    print("No strings entered")
