def sumdigits (num):
    num = str(num)
    if len(num) == 0:
        return 0
    return int(num[:1]) + sumdigits(num[1:])