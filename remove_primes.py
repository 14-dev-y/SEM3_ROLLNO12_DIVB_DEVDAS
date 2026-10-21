def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

numbers = list(range(1, 21))
numbers = [number for number in numbers if not is_prime(number)]
print("After removing primes:", numbers)
