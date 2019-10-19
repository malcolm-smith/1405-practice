# Pset 5 Problem 4
# Binary Quiz Game - **

import math 
import random

# Returns largest power of 2 less than or equal to n
def pow2(n):
	if n < 0:
		raise ValueError("Positive integers only. ")
	return 2**(int(math.log(n, 2))) # returns 2 raised to truncated log base 2


# Returns binary conversion (string) of a decimal 
def decToBin(n):
	x = float(n) 
	p = pow2(x) 
	output = ""

	while p > 0: 
		if p <= x: 
			x = x -float(p)
			output += "1"
		else:
			output += "0"
		p = p // 2

	return output
	

# Returns users guess of binary value of chosen integer 
def userBin(n):
	print("\nThe number is: " + str(n))
	bin_val = input("Enter the corresponding binary value: ")
	return bin_val


def main():

	flag = True
	rand = random.randint(-1, 257) # Random number from [0, 257]
	guess = userBin(rand)
	score = 0

	while flag:
		if guess == decToBin(rand):
			score += 1
			print("Correct!")
		elif guess == "stop":
			print("\nGame over. Your score is: " + str(score))
			flag = False
		else:
			print("Wrong!")
			
		rand = random.randint(-1, 257)
		guess = userBin(rand)


if __name__ == "__main__":
	main()