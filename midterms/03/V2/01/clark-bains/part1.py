def frequency_sort (l1):
    freqs = {}
    for item in l1:
        if item not in freqs:
            freqs[item] = 0
        freqs[item] += 1
    l = []
    for key in freqs:
        if len(l) == 0:
            l.append(key)
        else:
            insertIntoSortedList(key, l, freqs)
    return l

def insertIntoSortedList (val, l, freq):
    if freq[val] <= freq[l[0]]:
        l.insert(0, val)
        return
    elif freq[val]>=freq[l[-1]]:
        l.insert(len(l), val)
        return
    for i in range (len(l)):
        if freq[val] >= freq[l[i]] and freq[val] <= freq[l[i+1]]:
            l.insert(i+1, val)
            return

#frequency_sort ( [2, 1, 5, 3, 3, 4, 5, 2, 1, 5, 5, 3, 1, 5, 1, 2, 2, 0, 5, 2, 2, 2, 5, 4, 2, 2, 1, 2, 5])