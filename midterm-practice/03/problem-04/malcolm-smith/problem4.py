def xmostfrequent(s, x):
    words = s.split(' ')
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    frequency = sorted(frequency, key=frequency.get, reverse=True)
    return frequency[:x]
