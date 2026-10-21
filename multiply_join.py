def operation(a,b):
    if isinstance(a,int) and not isinstance(a,bool) and isinstance(b,int) and not isinstance(b,bool): return a*b
    return str(a)+str(b)
calculate=lambda a,b:operation(a,b)
print("Integer example:",calculate(5,4))
print("Name example:",calculate("Dev","Tanish"))
