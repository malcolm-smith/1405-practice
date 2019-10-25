# Pset 6 Problem 4
# Largest volume

# Return largest volume from list of box dimensions
def max_volume(nums):
	volumes = []
	for box in nums:
		volumes.append(box[0]*box[1]*box[2])

	maximum = volumes[0]
	for volume in volumes:
		if volume > maximum:
			maximum = volume

	return maximum


def main():
	# Test case
	boxes = [[3, 4, 2], [6, 4, 1], [5, 5, 5]]
	largest = max_volume(boxes)
	print("Largest volume: " + str(largest))

if __name__ == '__main__':
	main()

