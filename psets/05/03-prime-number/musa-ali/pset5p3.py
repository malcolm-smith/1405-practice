# Pset 5 Problem 3
# Prime Number Function - *

from math import sqrt

def isPrime(n):
	if n == 2 or n == 3: return True # 2 and 3 are the first prime numbers
	if n % 2 == 0 or n < 2: return False # disregard even numbers and 0, 1
	for x in range(3, int(sqrt(n))+1, 2): # only checks odd numbers
		if n % x == 0:
			return False

	return True

for i in range(1, 101):
	if isPrime(i):
		print(i, end=" ")
