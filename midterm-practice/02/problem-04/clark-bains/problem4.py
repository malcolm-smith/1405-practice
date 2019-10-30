def gcd(num2, num1):
    highestFound = -1
    if (num1 < 1 or num2 <1 ):
        return -1 
    for i in range(1,num2+1):
        if num2%i==0 and num1%i==0:
            highestFound = i

    return highestFound

print (gcd(20, 30))