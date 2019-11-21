# PM3 Problem 3

def jaccard(lst1, lst2):
	union = []
	intersection = []
	for i in lst1:
		if i not in union:
			union.append(i)
		if i in lst2 and i not in intersection:
			intersection.append(i)
	for i in lst2:
		if i not in union:
			union.append(i)
		if i in lst1 and i not in intersection:
			intersection.append(i)
	return len(intersection)/len(union)