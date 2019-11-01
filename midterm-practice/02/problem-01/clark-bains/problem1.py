import random
rand = random.randrange(0,100)
guess = None
while guess != rand:
    guess  = int(input("Enter A guess: "))
    if guess-rand > 0:
        print ("Lower")
    elif guess-rand < 0:
        print ("Higher")

print ("Good.")