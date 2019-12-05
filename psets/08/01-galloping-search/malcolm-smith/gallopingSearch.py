def gallopingsearch(list, searchvalue):
    start, end = 0, 1
    while (end < len(list)) and (list[end] < searchvalue):
        start = end
        end = end * 2
    return searchvalue in list[start:end+1]


print(gallopingsearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 11, 13, 14], 13))
