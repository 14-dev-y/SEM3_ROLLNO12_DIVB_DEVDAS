def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
n=int(input("Dev, number to check: "))
print("Prime" if is_prime(n) else "Not prime")
a=int(input("Range start: ")); b=int(input("Range end: "))
print("Primes in range:",[x for x in range(a,b+1) if is_prime(x)])
