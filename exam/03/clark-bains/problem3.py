#O(n), since it has a flat structure, and all nested operations are O(1)
def jaccard (l1,l2):
    intersect = {}
    intersectionLength = 0
    for val in l1:
        intersect[val] = 1
    for val in l2:
        if val in intersect:
            if intersect[val] == 1:
                intersectionLength+=1
                intersect[val]+=1
    union = {}
    for val in l1+l2:
        union[val] = 1
    unionLength=0
    for key in union:
        unionLength +=1

    return intersectionLength/unionLength
