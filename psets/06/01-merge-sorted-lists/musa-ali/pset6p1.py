# Pset 6 Problem 1
# Merge 2 lists into one ascending order list

# Take 2 sorted lists, merge into one sorted list
def merge_lists(l1, l2):
	unsorted_merged = l1 + l2
	sorted_merged = []

	i = 0
	size = len(unsorted_merged)

	# Appends smallest elements from unsorted merged list to the sorted merged list
	while i != size:
		smallest = min(unsorted_merged)
		sorted_merged.append(smallest)
		unsorted_merged.remove(smallest)
		i += 1

	return sorted_merged


def main():
	# Test cases
	l1 = [1, 3, 5]
	l2 = [2, 4, 6]
	print(merge_lists(l1, l2))


if __name__ == '__main__':
	main()