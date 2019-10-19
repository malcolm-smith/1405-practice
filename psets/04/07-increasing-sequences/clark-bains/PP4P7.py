filename = input ("File name: ")
file = open (filename, "r")
currentIncreasingTrendLength = 1
currentDecreasingTrendLength = 0
maxPos = 0
previousNumber = None
for line in file:
    currentNumber = int(line.strip())
    if previousNumber == None:
        previousNumber = currentNumber
    if currentNumber > previousNumber:
        currentIncreasingTrendLength += 1
        currentDecreasingTrendLength = 0
        
    elif currentNumber < previousNumber:
        currentDecreasingTrendLength +=1
        maxPos = maxPos if currentIncreasingTrendLength<maxPos else currentIncreasingTrendLength
        currentIncreasingTrendLength = 1
    if currentDecreasingTrendLength > 3:
        break
    previousNumber = currentNumber

maxPos = maxPos if currentIncreasingTrendLength<maxPos else currentIncreasingTrendLength
print ("Length of longest increasing sequence is " + str(maxPos))

