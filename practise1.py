"""
COUNT UPPERCASE LOWERCASE - done
SEARCHED WORDS - done
COPY 1 FILE INTO ANOTHER FILE - done
WRITE OPEN CLOSE FILE - done
SPLIT WORDS AND COUNTED  -done
CHARACTRS IN A FILE - done
LINE COUNT VOWELS COUNT - done
READ LINES - done
SYMBOL SPECIAL CHARACTER DIGIT COUNT - done
REPLACE
"""

f = open("words.txt", "w")

for i in range(3):
    word = input("ENTER WORDS IN A FILE: ")
    f.write(word + "\n")

f.close()


f1 = open("words.txt", "r")
data = f1.read()

print("\nCHARACTERS IN FILE:", len(data))
print("HOW MANY WORDS:", len(data.split()))


upper_count = 0
lower_count = 0

for ch in data:
    if ch.isupper():
        upper_count += 1

    if ch.islower():
        lower_count += 1

print("HOW MANY UPPERCASE LETTERS:", upper_count)
print("HOW MANY LOWERCASE LETTERS:", lower_count)


linecount = data.count("\n")
print("HOW MANY LINES:", linecount)


count = 0

for ch in data:
    if ch in "aeiouAEIOU":
        count += 1

print("VOWELS IN FILE:", count)


search_word = input("\nENTER WORD TO SEARCH: ")

if search_word in data.split():
    print("WORD FOUND")
else:
    print("WORD NOT FOUND")

f1.close()


f1 = open("words.txt", "r")
f2 = open("copy.txt", "w")

data = f1.read()
f2.write(data)

f1.close()
f2.close()

print("FILE COPIED SUCCESSFULLY")


f1 = open("words.txt", "r")
l1 = f1.readlines()
print(l1)
for index, line in enumerate(l1, start=1):
    print(f"Line {index}: {line.strip()}")
f1.close()  

special_count = 0
digit_count = 0
space_count = 0

for ch in data:
    if ch.isdigit():
        digit_count += 1
    elif ch == " ":
        space_count += 1
    else:
        special_count += 1

print("DIGITS IN FILE:", digit_count)
print("BLANK SPACES IN FILE:", space_count)
print("SPECIAL CHARACTERS IN FILE:", special_count)