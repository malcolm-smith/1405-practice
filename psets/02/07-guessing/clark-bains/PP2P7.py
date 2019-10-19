import math, random
rand = random.randint(1,100)
guess = int(input ("Guess Num: "))
#Ternary operators make for extra unreadablity. Darn you python
print ("You were right" if rand==guess else ("You were off by " + str (abs (rand-guess))))