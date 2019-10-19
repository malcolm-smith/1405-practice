# Pset 4
# Problem 11
# 'Search Engine'

# Returns the names of the files from pages.txt
def get_files():
	files = []
	for line in open('pages.txt', 'r'):
		files.append(line.strip())

	return files

# Returns the count of how many times a specific word appears in each file
def get_word_count(word, files):
	freqs = []
	for file in files:
		max_count = 0
		count = 0
		for line in open(file, 'r'):
			if line.strip() == word:
				count += 1
		freqs.append([file, count])

	return freqs

# Returns the file, count where the specific word appears the most
def get_max_freqs(word, files):
	freqs = get_word_count(word, files)
	max_count = 0
	i = 0
	for freq in freqs:
		if int(freqs[i][1]) > max_count:
			max_count = int(freqs[i][1])
			max_page = freqs[i][0]
		i += 1

	return (max_page, max_count)

# Returns the file, ratio of word count against number of lines in the file
def get_ratio(word, files):

	freqs = get_word_count(word, files)
	count = 0

	for file in files:
		total_lines = 0
		# Gets the number of lines from each file
		for line in open(file, 'r'):
			total_lines += 1

		# Gets how many times specific word appears in each file
		word_count = freqs[count][1]
		count += 1

		# Calculate the ratio from each file and append to a list
		ratio = word_count / total_lines
		ratios.append([file, ratio])

	ratios = []
	max_ratio = 0

	# Get max ratio, page
	for ratio in ratios:
		if ratio[1] > max_ratio:
			max_ratio = ratio[1]
			max_page = ratio[0]

	return (max_page, max_ratio)


def main():
	while True:
		word = input("\n   Enter a word to search for: ")
		if word == 'q':
			break
		files = get_files()
		freqs = get_max_freqs(word, files)
		ratios = get_ratio(word, files)
		print("   Max Page (Count): " + freqs[0])
		print("   Max Count: " + str(freqs[1]))
		print("   Max Page (Ratio): " + ratios[0])
		print("   Max Ratio: " + str(ratios[1]))

if __name__ == '__main__':
	main()