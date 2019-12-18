def xmostfrequent (words,x):
    l = words.split(" ")
    freqs = {}
    for elm in l:
        if elm not in freqs:
            freqs[elm] = 0 
        freqs[elm] += 1
    newList = []
    for i in range(x):
        maxVal = 0
        maxKey = ""
        for key in freqs:
            if freqs[key]>maxVal:
                maxKey = key
                maxVal = freqs[maxKey]
        newList.append (maxKey)
        del freqs[maxKey]
    return newList