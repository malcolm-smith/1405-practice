guess = 73
close_range = 10
far_range = 20
user_guess = int(input("Guess a number: "))
if guess == user_guess:
    print ("Correct!")
elif abs(user_guess-guess)<close_range:
    print ("Close but not quite correct")
elif abs(user_guess-guess)<far_range:
    print ("Nice try, but you are far away")
else:
    print ("You are not very good at this.")