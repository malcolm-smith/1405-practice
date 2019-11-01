def analyze (filename):
    f = open (filename, 'r')
    consecutive = 0
    longestConsecutive = 0
    for line in f:
        if int(line.strip())%2 ==0:
            consecutive += 1
        else:
            if consecutive > longestConsecutive:
                longestConsecutive = consecutive
            consecutive = 0
    f.close()
    return longestConsecutive
print (analyze("..\\resources\\nums.txt"))