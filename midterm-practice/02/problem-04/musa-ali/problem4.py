# Practice Midterm 2
# Greatest Common Divisor

import math

# Returns the greatest common divisor between two integers
def gcd(a, b):
	if a < 1 or b < 1:
		return -1

	divs_a = []
	for i in range(1, a + 1):
		if a % i == 0:
			divs_a.append(i)

	divs_b = []
	for i in range(1, b + 1):
		if b % i == 0:
			divs_b.append(i)

	common = []
	for num in divs_a:
		if num in divs_b:
			common.append(num)

	return max(common)

def main():
	a = int(input("Enter first number: "))
	b = int(input("Enter second number: "))
	gcd_ab = gcd(a, b)
	print("The Greatest Common Divisor between " + str(a) + " and " + str(b) + " is " + str(gcd_ab))

if __name__ == '__main__':
	main()