# PM 3 Problem 4

def xmostfrequent(s, x):
	freqs = {}
	for word in s.split():
		if word not in freqs:
			freqs[word] = 1
		else:
			freqs[word] += 1

	freqs_list = []
	while len(freqs_list) < x:
		largest = 0
		largest_word = ''
		for word in freqs:
			if freqs[word] > largest:
				largest = freqs[word]
				largest_word = word

		del freqs[largest_word]
		freqs_list.append(largest_word)

	return freqs_list
