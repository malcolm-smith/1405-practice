def minarea(l1):
    dimarea = []
    for dims in l1:
        dimarea.append([dims[0]*dims[1]*.5, dims])
    minset = dimarea[0]
    for areadimset in dimarea:
        if areadimset[0] <= minset[0]:
            minset = areadimset
    return minset[1]
