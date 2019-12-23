'''
This runs in O(n) time, where n is the combined length of a and b.
This is because by creating sets containing the values of a & b, checking to see "if x in b" runs in O(1) time instead of O(n) time
(sets are hashed 1D collections, hash lookup is O(1))
Moreover, the sets for union/intersection allow for automatic handling of duplicates in O(1) time as well.
Because there is two separate for loops, each running in "O(a)" and "O(b)" time respectively, this runs in O(a+b) time - more simply, O(n).
'''
def jaccard(a,b):
    aSet = set(a)
    bSet = set(b)
    union = set()
    intersection = set()
    for x in a:
        union.add(x)
        if x in b:
            intersection.add(x)

    for x in b:
        union.add(x)
    # handles div by zero errors
    if len(union) == 0: return 0
    return len(intersection) / len(union)
