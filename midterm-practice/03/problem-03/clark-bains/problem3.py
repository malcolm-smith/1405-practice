def jaccard(l1,l2):
    unique1={}
    unique2={}
    uniqueInBoth = 0
    for val in (l1):
        unique1[val] = 1
    for val in (l2):
        unique2[val] = 1
    for val in unique1:
        if val in unique1 and val in unique2:
            uniqueInBoth+=1
    unique = {}
    for val in (l1+l2):
        unique[val] = 1
    return uniqueInBoth/len(unique)
