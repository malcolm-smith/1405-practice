def lettercount (inStr):
    freq = {}
    for let in inStr:
        if let not in freq:
            freq[let] = 1
        else:
            freq[let]+=1
    return freq
print(lettercount("dasd"))