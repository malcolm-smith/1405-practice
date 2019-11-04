def isPrime (num):
    divisors = []
    for i in range (1, num+1):
        if num%i==0:
            divisors.append(i)
        if (len(divisors)>2):
            return False
    return (len(divisors)==2)

for i in range (0,101):
    print (str(i) + ": " + ("prime" if isPrime(i) else "not prime"))