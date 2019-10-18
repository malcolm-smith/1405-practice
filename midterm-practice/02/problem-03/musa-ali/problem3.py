# Practice Midterm 2
# Analyze Evens

# Return longest consequtive sequence of even numbers in a file
def analyze(file):
	with open(file, "r") as fin:

		# Adds numbers from file into a list
		nums = []
		for line in fin:
			for num in line:
				if num != ' ':
					nums.append(int(num))

		# Find index of first even number of the sequence, count of of how many nums in the sequence
		seq_max = [-1, -1]
		index = 0
		count = 0
		i = 0
		for num in nums:
			if num % 2 == 0:
				count += 1
				if count > seq_max[1]:
					seq_max = (index, count)
			else:
				index = i + 1
				count = 0
			i += 1

		# Adds the sequence to a list
		seq_len = seq_max[1]
		seq_nums = []
		seq_index = seq_max[0]
		for num in range(seq_max[1]):
			seq_nums.append(nums[seq_index + num])

		sequence = [seq_nums, seq_len]

		return sequence


def main():

	filename = "nums.txt"
	seq = analyze(filename)
	print("The longest sequence of even length is of length: " + str(seq[1]))
	print("The sequence is: " + str(seq[0]))

if __name__ == '__main__':
	main()

