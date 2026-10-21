def convert(s):
    try: return int(s)
    except ValueError:
        try: return float(s)
        except ValueError: return s
a=convert(input("Enter first value (e.g. Dev or 10): "))
b=convert(input("Enter second value (e.g. Tanish or 5): "))
print("Types:",type(a).__name__,type(b).__name__)
if isinstance(a,str) and isinstance(b,str): print("+:",a+b," *:",a*3)
elif isinstance(a,(int,float)) and isinstance(b,(int,float)): print("+:",a+b," *:",a*b)
else: print("Use values of compatible types for + and *")
