# find the number of digits of an integer


num = int(input('Enter an integer: '))

if num == 0:
    num += 1  # this test case does not work

digits = 0

while num > 1 or num < -1:  # can handle negative integers
    num = num / 10
    digits += 1

print('There are %d digits in that number.' % digits)
