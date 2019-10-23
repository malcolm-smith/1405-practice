# finds GCD using Euclid's Algorithm (https://en.wikipedia.org/wiki/Euclidean_algorithm)
# is recursive (https://en.wikipedia.org/wiki/Recursion_(computer_science))
def gcd(a, b):
    if a % b == 0:
        return b
    if b > a:
        return gcd(b, a)
    return gcd(b, a % b)


print(gcd(20, 24))
