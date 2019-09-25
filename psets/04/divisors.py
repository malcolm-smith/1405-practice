def solutionA():
    num = int(input('Enter an integer: '))
    x = 1
    divisors = []
    sum = 0

    print('The divisors are:')

    while x <= num:
        if num % x == 0:
            sum += x
            divisors.append(x)
            print(x)
        x += 1

    print('The sum of the divisors is %d' % sum)
    if len(divisors) > 2:
        print('The number is not prime')
    else:
        print('The number is prime')


def solutionB():
    num = int(input('Enter an integer: '))
    sum = num + 1

    print('The divisors are:\n1')
    for i in range(2, num):
        if num % i == 0:
            print(i)
            sum += i
    print(num)

    print('The sum of the divisors is %d' % sum)
    if sum == num + 1:
        print('The number is prime')
    else:
        print('The number is not prime')
