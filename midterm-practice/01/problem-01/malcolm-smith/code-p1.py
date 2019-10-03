num = int(input('Please enter an integer: '))

words = str.split(input('Enter three words: '), ' ')

for word in words:
    if (len(word) % num) == 0:
        print(word)
