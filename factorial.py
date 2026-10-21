def factorial(n):
    if n<0: return None
    result=1
    for i in range(1,n+1): result*=i
    return result
n=int(input("Dev, enter non-negative integer: "))
print("Factorial is not defined for negative numbers" if factorial(n) is None else factorial(n))
