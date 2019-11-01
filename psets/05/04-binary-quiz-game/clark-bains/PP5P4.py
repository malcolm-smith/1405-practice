import math, random
def pow2 (num):
    return int(2**(math.log2(int(num))//1))
def decToBin(dec):
    binStr = "0b"
    currentLog = math.log2(pow2(dec))
    while currentLog !=-1:
        if 2**currentLog <= dec:
            dec -=2**currentLog
            binStr+="1"
        else:
            binStr+="0"
        currentLog -=1
    return binStr
def userBin (num):
     return input ("Enter " + str(num) + " as a binary number (0b) form: ")    
score = 0
while True:
    num = random.randrange(0,257)
    userInput = userBin (num) 
    score+= 1 if decToBin(num) == userInput else 0
    if 'stop' in userInput.lower():
        break

print ("Score is " + str(score))

        
