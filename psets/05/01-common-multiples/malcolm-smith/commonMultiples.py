def ismultiple(a, b):
    return b % a == 0

def commonmultiple(a, b, c):
    return ismultiple(a, c) and ismultiple(b, c)

a = int(input('Enter two numbers:\n1) '))
b = int(input('2) '))

for i in range(1, 101):
    if commonmultiple(a, b, i):
        print('%d is a common multiple' % i)