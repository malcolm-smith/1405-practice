# Practice Midterm 2
# Problem 1
# Guessing Game

import random

# Checks user guess against random number
def check_guess(num):
	while True:
		try:
			guess = int(input("Enter a guess: "))
			if guess < num:
				print("Guess higher!")
			elif guess > num:
				print("Guess lower!")
			else:
				print("You win!")
		except ValueError:
			print("Enter a valid guess.")


def main():
	num = random.randint(0, 100)
	check_guess(num)


if __name__ == '__main__':
	main()