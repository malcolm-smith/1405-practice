filename = input ("Enter File Name: ")
largestNum = None
smallestNum = None
numPositive = 0
numNegative = 0
n = 0
sum = 0
file = open(filename, 'r')
for line in file:
    line = int(line.strip())
    sum +=line
    n +=1
    if largestNum == None or smallestNum == None:
        largestNum = line
        smallestNum = line
    if line > largestNum:
        largestNum = line
    elif line < smallestNum:
        smallestNum = line
    if line > 0:
        numPositive +=1
    elif line < 0: 
        numNegative +=1
        print()
print ("Largest Number =", largestNum)
print ("Smallest Number =", smallestNum)
print ("Average Value =", sum/n)
print ("Positive Numbers =", numPositive)
print ("Negative Numbers =", numNegative) 