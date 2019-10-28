# Pset 6 Problem 2
# Storing sensor data

# Add new measurements, update list accordingly
def measure(int):
	global data
	global X

	data.append(int)
	# 1 2 3 50 0 5
	# X = 5
	# Want: 2 3 50 0 5

	# If data has more measurements than X, update list to only include newest X measurements
	if len(data) + 1 > X:
		data = data[len(data)-X:]

	return data

# Returns average of measurements
def average():

	count = len(data)
	total = 0
	for x in data:
		total += x

	return total / count

# Returns minimum of measurements
def min():
	minimum = data[0]
	for x in data:
		if x < minimum:
			minimum = x

	return minimum

# Returns maximum of measurements
def max():
	maximum = data[0]
	for x in data:
		if x > maximum:
			maximum = x

	return maximum

# Checks difference between max, min to see if it is >10
def is_danger():
	minimum = min()
	maximum = max()
	if (maximum - minimum) > 10:
		return True
	else:
		return False


def main():
	# Test cases
	global data, X
	data = [1, 2, 3, 50, 0]
	num = int(input("Enter measurement: "))
	X = int(input("Enter memory specification: "))
	print("Old Data: " + str(data))
	print("New Data: " + str(measure(num)))
	print("Average: " + str(average()))
	print("Minimum: " + str(min()))
	print("Maximum: " + str(max()))
	print("Danger?: " + str(is_danger()))


if __name__ == '__main__':
	main()