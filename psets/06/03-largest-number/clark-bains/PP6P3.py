def maxVal(listIn):
    maxVal = None if not len(listIn) else listIn[0]
    for val in listIn[1:]: #I already checked, [][1:]=[], so this is safe
        maxVal = val if val>maxVal else maxVal
    return maxVal

print (maxVal([10,45,10,34]))