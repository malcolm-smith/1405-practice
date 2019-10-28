def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(101):
    if isPrime(i):
        print('%d is a prime number' % i)