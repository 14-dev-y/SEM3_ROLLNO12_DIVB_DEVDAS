words=["level","Dev","madam","Tanish","radar","civic"]
print("Palindromes:",list(filter(lambda word:word.lower()==word.lower()[::-1],words)))
