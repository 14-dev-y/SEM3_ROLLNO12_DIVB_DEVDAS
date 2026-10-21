def binary(n): return bin(n)[2:]
def octal(n): return oct(n)[2:]
def hexadecimal(n): return hex(n)[2:].upper()
n=int(input("Dev, enter decimal integer: "))
print("Binary:",binary(n)); print("Octal:",octal(n)); print("Hexadecimal:",hexadecimal(n))
