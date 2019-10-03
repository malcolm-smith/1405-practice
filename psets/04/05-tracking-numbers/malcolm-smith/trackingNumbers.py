import sys

num = 0
sumOfNums = 0
counter = 0
largestNum = -sys.maxsize
smallestNum = sys.maxsize
positiveNums = 0
negativeNums = 0

while num != 'q':
    num = input('Enter an integer (\'Q\' to quit): ')
    if num != 'q':
        num = int(num)
        sumOfNums += num
        if num > largestNum:
            largestNum = num
        if num < smallestNum:
            smallestNum = num
        if num >= 0:
            positiveNums += 1
        else:
            negativeNums += 1
        counter += 1

print('Numbers entered:\t%d\nAverage:\t\t%d\nLargest Number:\t\t%d\nSmallest Number:\t%d\n' %
      (counter, (sumOfNums / counter), largestNum, smallestNum))
