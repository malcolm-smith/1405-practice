def multiply(a, b):
    if a == 1:
        return b
    elif a == 0:
        return 0
    else:
        return b + multiply(a - 1, b)

print(multiply(2, 32))
