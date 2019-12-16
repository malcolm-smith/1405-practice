# Runs in O(n) time. Has a flat structure, comprised of looping over elements, O(n)
# Any nested methods, operations, comparisons are O(1), line  x in dict(), addition, assignment, conditionals
# 
def jaccard (l1,l2):
    intersection = {}
    for elm in l1:
        intersection[elm] = 1
    for elm in l2:
        if elm in intersection:
            intersection[elm] += 1
    intersectionCount = 0
    for key in intersection:
        if intersection[key]>1:
            intersectionCount+=1
    union = {}
    for elm in l1+l2:
        union[elm] = 0
    unionCount = 0
    for key in union:
        unionCount+=1
    return intersectionCount/unionCount
