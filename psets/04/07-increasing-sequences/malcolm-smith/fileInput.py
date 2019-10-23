def sequenceLength(filename):
    count = 1
    longest = 0
    previous = -1
    for line in open(filename):
        if int(line) > previous:
            count += 1
        else:
            if count > longest:
                longest = count
            count = 1
        previous = int(line)
    if count > longest:
        return count
    return longest

print(sequenceLength('sequence1.txt'))
print(sequenceLength('sequence2.txt'))
