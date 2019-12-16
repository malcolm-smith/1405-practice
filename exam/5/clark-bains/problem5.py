def kthsmallest (l1,k):
    copy = l1[:]
    for i in range(k):
        smallest = copy[0]
        smallestIdex = 0
        for o in range(len( copy)):
            if copy[o] <= smallest:
                smallest = copy[o]
                smallestIdex = o
        copy.pop(smallestIdex)
    return smallest

