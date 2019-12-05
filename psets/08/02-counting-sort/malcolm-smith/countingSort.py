def countingSort(list):
    returnlist = []
    # find frequency of each value in list
    freq = {}
    for i in list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    # sort unique values
    newlist = sorted(freq.keys())
    # generate new list by adding frequency of each occurence
    for i in newlist:
        for j in range(0, freq[i]):
            returnlist.append(i)
    return returnlist
