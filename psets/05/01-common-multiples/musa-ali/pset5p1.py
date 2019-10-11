# Pset 5 Problem 1
# Common Multiples - *

# Checks if b is a multiple of a
def ismultiple(a, b):
	if b % a == 0: return True
	else: return False

# Checks if c is a multiple of both a and b
def commonmultiple(a, b, c):
	if ismultiple(a, c) and ismultiple(b, c):
		return True
	else:
		return False

# Prints all numbers between 1 and 100 (inclusive)
# that are common multiples of a and b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
for i in range(1, 101):
	if commonmultiple(a, b, i):
		print(i, end=" ")