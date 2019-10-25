from random import randint

def pow2(n):
    for i in range(n, 0, -1):
        if (i & (i - 1)) == 0:
            return i

def decToBin(n):
    binaryString = ''
    p = pow2(n)
    while p != 0:
        if p <= n:
            n = n - p
            binaryString = binaryString + '1'
        else:
            binaryString = binaryString + '0'
        p = p // 2
    return binaryString

def userBin(num):
    return input('What is %s in binary?\n' % num)

def main():
    score = 0
    guess = ''
    while guess != 'stop':
        answer = randint(0, 256)
        guess = userBin(answer)
        if guess == decToBin(answer):
            score += 1
    print('Your score was: %d' % score)

main()