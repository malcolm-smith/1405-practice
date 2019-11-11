def intersection(a, b):
    new = []
    for i in a:
        if i in b and i not in new:
            new.append(i)
    return new

def union(a, b):
    new = []
    for i in a:
        if i not in new:
            new.append(i)
    for i in b:
        if i not in new:
            new.append(i)
    return new

def jaccard(a, b):
    return len(intersection(a, b)) / len(union(a, b))
