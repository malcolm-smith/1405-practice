def mergelists(a, b):
    if a and b:
        if a[0] > b[0]:
            a, b = b, a
        return [a[0]] + mergelists(a[1:], b)
    return a + b

print(mergelists([1, 2, 4], [0, 3, 5]))
