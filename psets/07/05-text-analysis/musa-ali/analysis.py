# Pset 7 Problem 5
# Text Analysis

freqs = {}
words = []

# Loads file
def load(filename):
	global words
	with open(filename, 'r') as f:
		words = f.read().split()


# Gets common word(s) from file
def commonword(arr):
	global words
	global freqs

	# return none if list is empty or not at least one match
	if not arr or not any(word in arr for word in words):
		return None
	# gets count for each word in list
	else:
		for word in words:
			if word not in freqs:
				freqs[word] = 0
			if word in freqs:
				freqs[word] += 1

	# get mini dict of counts
	counts_dict = {}
	for word in arr:
		if word not in counts_dict:
			counts_dict[word] = freqs[word]
	
	# get max count
	max_val = -1
	max_key = None
	for key in counts_dict:
		if counts_dict[key] > max_val:
			max_val = counts_dict[key]
			max_key = key

	freqs = {}
	return max_key


# Get most common word after a specific word
def commonpair(word):

	counts = {}
	# word not in file or is the last word
	if word not in words or word not in (words[:len(words)-1]):
		return None

	# update dictionary with counts
	for i in range(len(words)-1):
		prev_word = words[i]
		next_word = words[i+1]
		if prev_word == word:
			if next_word not in counts:
				counts[next_word] = 0
			if next_word in counts:
				counts[next_word] += 1

	# get word with biggest count
	max_val = -1
	max_key = None
	for key in counts:
		if counts[key] > max_val:
			max_val = counts[key]
			max_key = key
	
	return max_key

# Gets word count of file
def countall():
	global words

	count = 0
	for word in words:
		count += 1
	return count


# Gets all unique words in file
def countunique():
	global words

	uniques = []
	count = 0
	for word in words:
		if word not in uniques:
			uniques.append(word)
			count += 1
	
	return count
