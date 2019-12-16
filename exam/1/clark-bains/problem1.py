def nextprime (n):
    n+=1
    while (not isprime(n)):
        n+=1
    return n
def isprime (n):
    for i in range (2,int((n**.5 + 1))):
        if ((n%i) == 0):
            return False
    return True