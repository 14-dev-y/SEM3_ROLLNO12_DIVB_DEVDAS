items=["Dev",12,"Tanish",7,"Maahi",20,"Pooja","Adishree"]
print("Strings:",list(filter(lambda x:isinstance(x,str),items)))
text=input("Enter text to extract vowels: ")
print("Vowels:",list(filter(lambda c:c.lower() in "aeiou",text)))
