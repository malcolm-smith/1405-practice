# PM 5

def isvalidseries(lst, x, SUM):
	# [8, 4, 8, 3, 1, 2, 7, 9] 3, 19
	for i in range(len(lst[:len(lst)-(x-1)])):
		total = 0
		j = 0
		k = i
		while j < x:
			total += lst[k]
			k += 1
			j += 1
		if total > SUM:
			return False
	return True
