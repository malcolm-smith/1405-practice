def most_frequent(file):
	with open(file, 'r') as f:
		freqs = {}
		line = f.readline()
		classification = line.split(',')[3]
		while line != '':
			if classification not in freqs:
				freqs[classification] = 1
			freqs[classification] += 1
			line = f.readline()
			if line != '':
				classification = line.split(',')[3]
	max_val = 0
	max_key = None
	for key in freqs:
		if freqs[key] > max_val:
			max_val = freqs[key]
			max_key = key

	return max_key
