# PM 3 Problem 4

def xmostfrequent(s, x):
	freqs = {}
	# Loop over every word in s.split(), which is the string converted to a list
	for word in s.split():
		# If the word is not already in the freqs dictionary, add it and give it a value of 1
		if word not in freqs:
			freqs[word] = 1
		# If the word is in the dictionary, increment its value by 1
		else:
			freqs[word] += 1

	freqs_list = []
	# While the length of freqs_list is less than x
	while len(freqs_list) < x:
		# Initialize largest and largest_word variables
		largest = 0
		largest_word = ''
		# Loop over every word in the freqs dictionary
		for word in freqs:
			# Get the largest value (freqs[word]) and the key associated with that value (word)
			if freqs[word] > largest:
				largest = freqs[word]
				largest_word = word

		# Delete the largest word from the dictionary because we will loop over the dictionary again
		# to get the next largest word (X times)
		del freqs[largest_word]
		
		# Append the largest word to the frequency list
		# Once this list has X elements, the while loop will end
		freqs_list.append(largest_word)

	return freqs_list