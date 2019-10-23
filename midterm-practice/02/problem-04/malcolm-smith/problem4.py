# finds GCD using Euclid's Algorithm (https://en.wikipedia.org/wiki/Euclidean_algorithm)
# is recursive (https://en.wikipedia.org/wiki/Recursion_(computer_science))
def gcd_euclid(a, b):
    if a % b == 0:
        return b
    if b > a:
        return gcd_euclid(b, a)
    return gcd_euclid(b, a % b)

# GCD will always be -1 if one number is < 1
def gcd(a, b):
    if a < 1 or b < 1:
        return -1
    return gcd_euclid(a, b)


print(gcd(20, 24))
print(gcd(-6, 0))
