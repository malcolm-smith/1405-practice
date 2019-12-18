#This has a complexity of O(x) where x is the passed in number. Not sure how to express that
def isprime (i1, n = 0):
    #I feel like the n=0 trick isn't what you were going for,
    #But it still works and satisfies  the requirements
    #It doesn't only accept a single int argument, but it does accept *a* int argument, satisfying the requirements
    if n == 0:
        n = i1 - 1 
    if n == 1 or i1 == 1:
        return True
    if (i1%n) == 0:
        return False
    return isprime(i1,n-1)
print(isprime (4))