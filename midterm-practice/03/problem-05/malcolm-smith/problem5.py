def isvalidseries(sequence, x, sum):
    for i in range(0, len(sequence) - x + 1):
        total = sequence[i]
        for j in range(1, x):
            total += sequence[i + j]
        if total > sum:
            return False
    return True
