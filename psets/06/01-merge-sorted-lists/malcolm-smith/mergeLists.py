def mergeLists(a, b):
    newList = []
    indexa = 0
    indexb = 0
    # merge algorithm from merge sort
    while indexa < len(a) and indexb < len(b):
        if a[indexa] < b[indexb]:
            newList.append(a[indexa])
            indexa += 1
        else:
            newList.append(b[indexb])
            indexb += 1

    # add remaining elements, will only execute
    # one of the two while loops
    while indexa < len(a):
        newList.append(a[indexa])
        indexa += 1
    while indexb < len(b):
        newList.append(b[indexb])
        indexb += 1
    return newList


print(mergeLists([1, 2, 5], [1, 4, 5, 5, 7]))