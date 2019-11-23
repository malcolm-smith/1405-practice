def frequency_sort(L):
	freqs = {}
	for num in L:
		if num not in freqs:
			freqs[num] = 1
		freqs[num] += 1

	freqs_list = []
	min_val, min_key = None, None
	length = len(freqs)

	while len(freqs_list) != length:
		for key in freqs:
			if min_val == None and min_key == None:
				min_val = freqs[key]
				min_key = key
			elif freqs[key] < min_val:
				min_val = freqs[key]
				min_key = key

		freqs_list.append(min_key)
		del freqs[min_key]
		min_val, min_key = None, None

	return freqs_list

