# Pset 6 Problem 5
# Top X

# Find X largest numbers in nums and append to new list of size X
def top_x(nums, X):
	largest = []
	i = 0
	while i < X:
		maximum = nums[0]
		for x in nums:
			if x > maximum:
				maximum = x
		largest.append(maximum)
		nums.remove(maximum)
		i += 1

	return largest


def main():
	# Test case
	nums = [8, 3, 1, 2, 9, 4, 5, 7, 6]
	X = 4
	print(str(X) + " largest numbers in " + str(nums) + ": " + 	str(top_x(nums, X)))

if __name__ == '__main__':
	main()
