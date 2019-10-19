# Pset 5 Problem 2
# Number of Digits Function - *

# Returns the number of digits in an integer
def numDigits(int):
	string = str(int)
	counter = 0
	for x in string:
		counter += 1
	return counter

print(numDigits(5000)) # returns 4
print(numDigits(150)) # returns 3
print(numDigits(12345678910)) # returns 11