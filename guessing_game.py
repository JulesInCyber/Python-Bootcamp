'''
A simple number-guessing game.
Written to implement and pracice loops
Program chooses a number between 1 and 10.
User tries to guess that number.
Game can be repeated after each round
'''

import random as rd

random_number = rd.randint(1,10)
user_guess = None

while True:
    user_guess = input("Guess a number between 1 and 10: ")
    print(f"DEBUG: {random_number}")
    user_guess = int(user_guess)
    if user_guess > random_number:
        user_guess = int(input("Too high! Guess again: "))
    elif user_guess < random_number:
        user_guess = int(input("Too low! Guess again: "))
    else:
        print(f"Great! You won!\nThe number was {random_number}!")
        play_again = input("Want to Play again? (y/n): ")
        if play_again == "y":
            random_number = rd.randint(1,10)
            user_guess = None
        else:
            print("Thanks for playing!\nBYE!")
            break