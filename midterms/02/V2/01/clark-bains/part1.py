def isPrime (num):
    divisors = []
    for i in range (1, num+1):
        if num%i==0:
            divisors.append(i)
    return (len(divisors)<=2)
def largest_prime_factor (num):
    for i in range(num, 0, -1):
        if (num%i==0 and isPrime(i)):
            return i

print(largest_prime_factor(31))