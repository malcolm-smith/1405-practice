def sequenceLength(filename):
    count = 0
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
    return longest

print(sequenceLength('sequence1.txt'))
print(sequenceLength('sequence2.txt'))