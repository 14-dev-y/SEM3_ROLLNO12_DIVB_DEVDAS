try:
    
    a=5, b=2, c=0
    f=int("abc")
    d=a+b
    e=a/c
    ans=a+b+c
    print(a)
    print(b)
    print(c)    
    print(d)
    print(e)
    print(ans)
    print(f)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid value encountered.")
    
print("dev")
print(d)