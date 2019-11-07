# Pset 7 Problem 1
# Counting Letters

def lettercount(string):
	freqs = {}
	for letter in string:
		if letter not in freqs:
			freqs[letter] = 0
		if letter in freqs:
			freqs[letter] += 1
	return freqs

print(lettercount(input("Enter a string: ")))
