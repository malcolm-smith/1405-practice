import random, re
def promptForInput (q, validation, err="Invalid, please re-enter: "):
    while True:
        ans = input(q)
        if validation(ans):
            break
        else:
            print (err)
    return ans
def numMatching (l1,l2):
    num = 0
    for i in range (len(l1)):
        num +=1 if int(l1[i])==int(l2[i]) else 0
    return num

key = []
for i in range (5):
    key.append(random.randint(0,9))
#print (key)
turns = 0

while True:
    turns +=1
    guess = promptForInput("Guess: ", lambda x: (type(x)==str and len(str(x))==5))
    #This is the one true way
    correct = numMatching(re.findall("(\d)?",guess)[0:-1],key)
    if correct == 5:
        print ("You won in %d turns"%(turns))
        break
    elif correct<5:
        print ("You got %d correct" %(correct))
        if turns > 10:
            print ("You Lose")
            break

