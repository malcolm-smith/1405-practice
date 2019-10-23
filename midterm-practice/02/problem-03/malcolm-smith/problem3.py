def analyze(filename):
    count = 0
    longest = 0
    nums = open(filename).readline().split(' ')
    for n in nums:
        if int(n) % 2 == 0:
            count += 1
        else:
            if count > longest:
                longest = count
            count = 0
    return longest

print(analyze('nums.txt'))