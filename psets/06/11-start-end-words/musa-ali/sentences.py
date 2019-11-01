# Pset 6 Problem 11
# Start and End Words

def startwords(string):
	words = string.split()
	starts = []
	starts.append(words[0])

	ends = endwords(string)
	i = 0
	for word in words:
		if i == len(words) - 1:
			break
		elif word[:-1] in ends:
			starts.append(words[i+1])
		i += 1

	return starts


def endwords(string):
	words = string.split()
	ends = []
	for word in words:
		if word[-1] == ".":
			ends.append(word[:-1])

	return ends

# Test
sentence = "This is a test. Then it is not. Test two."
print("Start words: " + str(startwords(sentence)))
print("End words: " + str(endwords(sentence)))