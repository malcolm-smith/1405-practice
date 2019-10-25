# guessing game
from random import randint

target = randint(0, 100)

guess = None
while guess != target:
    guess = int(input('Make a guess:\t'))
    if guess > target:
        print('Too high!')
    elif guess < target:
        print('Too low!')

print('You win!')