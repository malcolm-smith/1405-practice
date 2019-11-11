# Pset 7 Problem 2
# Dictionaries and Caching
import time

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

def cachedfactorial(n, dic):

	mydict = dic

	# If dictionary is empty
	if not dic:
		# Cache individual factorials from n to 1
		for i in range(n):
			mydict[i] = factorial(i)	

	orderdic = []
	# get highest cached factorial
	for key in mydict:
		orderdic.append(key)
	highest_fact = orderdic[0]

	# If dictionary is not empty, 
	if dic:
		# Dictionary was previously added to, so use cached factorials in new calculation
		for n in range(highest_fact+1, n+1):
			diff = n - highest_fact
			multiplied = 1
			for i in range(n, n-diff, -1):
				multiplied *= i
			mydict[n] = multiplied * mydict[highest_fact]

	return mydict

mydict = {}
cachedfactorial(10, mydict)
start = time.time()
print(cachedfactorial(25, mydict))
end = time.time()
start2 = time.time()
print(factorial(25))
end2 = time.time()

print("cached takes: " + str(end-start) + " seconds...")
print("factorial function takes " + str(end2-start2) + " seconds...")