# Pset 6 Problem 3
# Largest number

# Returns largest value in list
def max_value(nums):
	maximum = nums[0]
	for x in nums:
		if x > maximum:
			maximum = x
	return maximum


def main():
	# Test case
	data = [63, 51, 122, 42, 30]
	print("Data: " + str(data))
	print("Largest value: " + str(max_value(data)))

if __name__ == '__main__':
	main()

