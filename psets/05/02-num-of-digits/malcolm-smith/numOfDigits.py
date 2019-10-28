from math import log10
from random import randint

def numDigits(n):
    return int(log10(n) + 1)

for i in range(10):
    num = randint(1, 10000)
    print('%d has %d digits' % (num, numDigits(num)))