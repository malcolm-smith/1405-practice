from random import randint

# all solutions in minimal lines because suffer


def problem1():
    # my first python program
    print('Hello World!')


def problem2():
    print(input('Prompt you want the user to see: '))


def problem3():
    print('Hello, %s. You are now %d years old.' % (input('What is your name?\t\t'), 2019 - int(input('What year were you born?\t'))))


def problem4():
    # convert metres to feet
    print('Feet:\t%.2f' % (int(input('Metres:\t')) * 3.32))


def problem5():
    print('volume = %d' % (int(input('length:\t')) + int(input('width:\t')) + int(input('height:\t'))))


def problem6():
    finalGrade = 0
    for i in range(1, 4):
        finalGrade += (int(input('Enter your #%d midterm grade:\t' % i)) * 0.2)
    finalGrade += (int(input('Enter your final grade:\t')) * 0.4)
    print(round(finalGrade, 4))


def problem7():
    print('You were %d away from the magic number' % abs(randint(1, 100) - int(input('Guess a number from 1-100: '))))


def problem8():
    print('Graphics are lame')
