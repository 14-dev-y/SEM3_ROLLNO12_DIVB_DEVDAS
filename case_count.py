def count_case(text):
    return sum(c.isupper() for c in text),sum(c.islower() for c in text)
text=input("Enter text, e.g. Dev and Tanish: ")
upper,lower=count_case(text)
print("Uppercase:",upper); print("Lowercase:",lower)
