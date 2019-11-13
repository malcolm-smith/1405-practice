from random import randint

def playmastermind():
    password = [randint(0, 9) for i in range(0, 5)]
    print(password)

    print("I've set my password, enter 5 digits in the range [0-9]separated by spaces(e.g. 1 3 2 4 4):")

    for i in range(1, 0, -1):
        guess = [int(i) for i in input('%d guesses remaining > ' % i).split(' ')]
        amountright = comparelists(password, guess)
        print('%d of 5 correct' % amountright)
        if amountright == 5:
            print('YOU WIN!!!')
            exit()
    print('\nOut of guesses.\nCorrect answer: ' + str(password) + '\nYou lose :(')


def comparelists(a, b):
    total = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            total += 1
    return total

playmastermind()