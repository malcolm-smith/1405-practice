def most_frequent(s1):
    f = open(s1,'r')
    classifications = {}
    for line in f:
        cl = line.split(',')[3]
        if cl not in classifications:
            classifications[cl] = 0
        classifications[cl] += 1
    mostVal = 0
    mostKey = ""
    f.close()
    for key in classifications:
            if classifications[key] >= mostVal:
                mostVal=classifications[key]
                mostKey = key
    return mostKey

        