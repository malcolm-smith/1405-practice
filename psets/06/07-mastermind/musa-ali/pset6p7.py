# Pset 6 Problem 7
# Mastermind

import random

# Generate random password
password = []
for i in range(5):
	password.append(random.randint(0,9))

guesses = 10
guess = []

print("I've set my password, enter 5 digits in the range [0-9] separated by spaces (e.g. 1 3 2 4 4):")
str_guess = input(str(guesses) + " guesses remaining > ")

# Keep checking guesses until all 10 guesses are used
while guesses > 1:

	# Convert user's guess into a list
	for i in str_guess:
		if i != ' ':
			guess.append(int(i))

	i = 0
	correct = 0
	# Check number of correct digits
	for num in guess:
		if guess[i] == password[i]:
			correct += 1
		i += 1
	print(str(correct) + " of 5 correct")

	if guess == password:
		print("You win!")
		break

	guesses -= 1

	guess = []
	str_guess = input(str(guesses) + " guesses remaining > ")

	if guesses == 1 and guess != password:
		print("You'll never get my treasure because the password was " + str(password))
