from math import floor

# simple integer calculator

operation = ''
int1 = None
int2 = None
operationList = (
    'ADDITION',
    'A',
    'SUBTRACTION',
    'S',
    'MULTIPLICATION',
    'M',
    'DIVISION',
    'D'
)

# program guide
print('Simple Integer Calculator\n')
print('(A)ddition\n(S)ubtraction\n(M)ultiplication\n(D)ivision (Long)')

# get user to choose operation
while operation not in operationList:
    operation = input('Please select an operation from the list above: ').upper()
    if operation not in operationList:
        print('This program does not support the operation "%s"' % operation)

# get numbers from user to operate function on
int1 = int(input('Please provide the 1st integer: '))
int2 = int(input('Please provide the 2nd integer: '))

# run operation and print results to the user
if operation[0] == 'A': # addition
    print('%d + %d = %d' % (int1, int2, (int1 + int2)))
elif operation[0] == 'S': # subraction
    print('%d - %d = %d' % (int1, int2, (int1 - int2)))
elif operation[0] == 'M': # multiplication
    print('%d * %d = %d' % (int1, int2, (int1 * int2)))
elif operation[0] == 'D': # long division
    print('%d / %d = %d with a remainder of %d' % (int1, int2, floor(int1 / int2), (int1 % int2)))