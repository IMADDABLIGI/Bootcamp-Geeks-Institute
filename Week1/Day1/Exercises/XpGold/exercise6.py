import random

user_input = int(input("Guess a number between 1 and 9: "))

random_number = random.randint(1, 9)

if user_input == random_number:
    print("Winner!")
else:
    print("Better luck next time.")
