givenYear = int(input('Leap Year Calculator\nEnter a year: '))

if givenYear % 400 == 0:
    print('%d is a leap year!' % givenYear)
elif givenYear % 100 == 0:
    print('%d is not a leap year!' % givenYear)
elif givenYear % 4 == 0:
    print('%d is a leap year!' % givenYear)
else:
    print('%d is not a leap year!' % givenYear)
