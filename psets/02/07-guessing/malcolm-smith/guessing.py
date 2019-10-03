from random import randint

print('You were %d away from the magic number' % abs(randint(1, 100) - int(input('Guess a number from 1-100: '))))
