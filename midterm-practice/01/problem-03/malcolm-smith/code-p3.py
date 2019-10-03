guess = 73
close_range = 10
far_range = 20

user_guess = None
while (user_guess != guess):
    user_guess = int(input('Make a guess: '))
    if user_guess == guess:
        print('Correct!')
    elif abs(guess - user_guess) <= close_range:
        print('Close but not quite correct.')
    elif abs(guess - user_guess) <= far_range:
        print('Nice try, but you are far away')
    else:
        print('You are not very good at this.')