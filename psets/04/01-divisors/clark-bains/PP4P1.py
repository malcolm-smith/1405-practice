def getPrimes (numberToTest):
    divisors=[]
    for i in range (1, numberToTest//2 + 1):
        if (numberToTest % i == 0):
            divisors.append(i)
    divisors.append(numberToTest)
    for num in divisors:
        print ("Found divisor", num)
    return divisors



num = input ("Enter a Number to check prime-arity: ")
divs = getPrimes(int(num))
print ("found", len(divs), "divisors, with a sum of", sum(divs))
if len(divs) == 2:
    print ("Number is prime")


