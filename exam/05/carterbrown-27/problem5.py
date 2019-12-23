# using a default argument.
def isprime(n,x=1):
    if n-x <= 1:
        return True
    return n % (n-x) > 0 and isprime(n,x+1)
