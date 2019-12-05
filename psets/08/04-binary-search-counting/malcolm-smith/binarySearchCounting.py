def count(list, value):
    startindex = findstart(list, value)
    # if no occurences of the number exist
    if startindex == -1:
        return 0
    endindex = findend(list, value)
    return endindex - startindex + 1

def findstart(list, value):
    start = 0
    end = len(list)-1

    while start <= end:
        midindex = int((start + end) / 2)
        midvalue = list[midindex]

        if midvalue == value:
            if list[midindex-1] != value:
                return midindex
            else:
                start -= 1
        elif midvalue < value:
            start = midindex + 1
        elif midvalue > value:
            end = midindex - 1
    # return -1 if no occurences are found
    return -1

def findend(list, value):
    list.append(None)
    start = 0
    end = len(list)-1

    while True:
        midindex = int((start + end) / 2)
        midvalue = list[midindex]

        if midvalue == value:
            if list[midindex+1] != value:
                return midindex
            else:
                end += 1
        elif midvalue < value:
            start = midindex + 1
        elif midvalue > value:
            end = midindex - 1

print(count([1, 1, 2, 2, 2, 2, 2, 3, 3, 3], 3))