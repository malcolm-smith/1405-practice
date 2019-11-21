# PM3 Problem 3

def jaccard(lst1, lst2):
	union = []
	intersection = []

    # Loop over every value in lst1
	for i in lst1:
        # Appends value to union if that value is not already in union
		if i not in union:
			union.append(i)
        # Appends value to intersection if the value is in both lst1 and lst2 and is not already in intersection 
        # (avoiding duplicates)
		if i in lst2 and i not in intersection:
			intersection.append(i)
            
    # Loop over every value in lst1
	for i in lst2:
        # Appends value to union if that value is not already in union
		if i not in union:
			union.append(i)
        # Appends value to intersection if the value is in both lst1 and lst2 and is not already in intersection 
        # (avoiding duplicates)
		if i in lst1 and i not in intersection:
			intersection.append(i)

	return len(intersection)/len(union)


