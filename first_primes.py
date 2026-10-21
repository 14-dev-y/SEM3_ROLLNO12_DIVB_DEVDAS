def is_prime(n):
    if n<2:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False
    return True
def GeneratePrime(n):
    primes=[]; value=2
    while len(primes)<n:
        if is_prime(value):primes.append(value)
        value+=1
    return primes
n=int(input("Dev, number of primes: "))
print(GeneratePrime(n) if n>=0 else "Enter zero or a positive number")
