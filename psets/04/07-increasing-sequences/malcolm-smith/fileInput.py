def sequenceLength(filename):
    count = 0
    longest = 0
    current = -1
    for line in open(filename):
        if int(line) > current:
            count += 1
        else:
            if count > longest:
                longest = count
            count = 1
        current = int(line)
    return longest

print(sequenceLength('sequence1.txt'))
print(sequenceLength('sequence2.txt'))