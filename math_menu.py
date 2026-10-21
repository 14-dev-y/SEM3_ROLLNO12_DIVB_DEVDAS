def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return "Cannot divide by zero" if b==0 else a/b
def int_div(a,b): return "Cannot divide by zero" if b==0 else a//b
def power(a,b): return a**b
while True:
    print("\nDev's Math Menu: 1 Add 2 Subtract 3 Multiply 4 Divide 5 Integer divide 6 Power 0 Exit")
    c=input("Choice: ")
    if c=="0": break
    if c not in "123456" or len(c)!=1: print("Invalid choice"); continue
    a=float(input("First number: ")); b=float(input("Second number: "))
    print({"1":add,"2":sub,"3":mul,"4":div,"5":int_div,"6":power}[c](a,b))
