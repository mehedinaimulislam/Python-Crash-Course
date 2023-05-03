# import necessary module
import random

# collect number range from user
starting_range = int(input("Enter starting range:- "))
ending_range = int(input("Enter ending range:- "))

# generating random number
random_number = random.randint(starting_range, ending_range)

# Make condition
while True:
	guess_number = int(input("Guess the number: "))
	if guess_number > random_number:
		print("Too High...")
	elif guess_number < random_number:
		print("Too Low...")
	else:
		print("Wow! You won the game.")
		break
