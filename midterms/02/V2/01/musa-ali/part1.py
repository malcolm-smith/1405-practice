# Get all factors of n
def get_factors(n):
	divs = []
	for i in range(1, n+1):
		if n%i == 0:
			divs.append(i)
	return divs

# Return largest prime factor 
def largest_prime_factor(nums):
	prime_facs = []
	for i in nums:
		if i == 1 or (len(factors(i)) == 2):
			prime_facs.append(i)

	return max(prime_facs)

# Get input from user, output largest prime factor for input
num = int(input("Enter an integer: "))
num_facs = get_factors(num)
largest = largest_prime_factor(num_facs)
print("The largest prime factor for " + str(num) + " is " + str(largest) + ".")