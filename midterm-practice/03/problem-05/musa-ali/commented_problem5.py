# PM 5

def isvalidseries(lst, x, SUM):
	''' Example input: ([8, 4, 8, 3, 1, 2, 7, 9], 3, 19)
	This means we are looking for (3) consecutive numbers that have a sum greater than 19.
	Since we are looking for (3) consecutive numbers, we must stop scanning the list once 
	we reach 2. This is because (2, 7, 9) is the last pair of 3 numbers we can check.

	This means we want to slice [8, 4, 8, 3, 1, 2, 7, 9] to change it to [8, 4, 8, 3, 1, 2].
	As we can see, we removed the last 2 elements. This is equal to x-1, where x in this case is 3.

	We want to keep the beginning of the list as is, so the code will be lst[:something].
	If we do lst[:len(lst)], which is lst[:8] in this case, we get an error because there is no index 8.
	This means we need to subtract from len(lst).
	We know we'll need to remove (x-1) elements from the END of the list, so we can use the following code:
	lst[:len(lst)-(x-1)]. In this case, this is lst[:8-(3-1)] or lst[:8-(2)] or lst[:6], which gives us [8, 4, 8, 3, 1, 2]. 
	The length of [8, 4, 8, 3, 1, 2] is 6, which is how many elements we want to now look at, so we use range(len(...)). '''

	# Explained above
	for i in range(len(lst[:len(lst)-(x-1)])):
		total = 0
		j = 0
		k = i # k = 0, 1, 2, ... len(lst) - 1
		# We only want to get the total of x consecutive numbers each time,
		# so if we have j = 0 and increment it each time we get the sum and then check if j is less than x,
		# we will always only get the sum of the required x consecutive numbers.
		while j < x:
			''' Example: x = 3
			If we are on the first index, 0, we want to get the sum of the 0th, 1st and 2nd index 
			So, while j < x, add to 'total' the values of lst[0], lst[1], lst[2]. This is done by
			incremeting k each time. '''
			total += lst[k]
			k += 1
			j += 1
		# If the sum of any 3 consecutive numbers is greater than the inputted SUM, return false
		if total > SUM:
			return False
	# Return True if no sum of any 3 consecutive numbers is greater than SUM
	return True
