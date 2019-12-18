def mode (l1):
    freqs = {}
    for elm in l1:
        if elm not in freqs:
            freqs[elm] = 0
        freqs[elm] += 1
    maxFreq = freqs[l1[0]]
    maxNum = l1[0]
    for key in freqs:
        if freqs[key] > maxFreq:
            maxFreq = freqs[key]
            maxNum = key
    return maxNum