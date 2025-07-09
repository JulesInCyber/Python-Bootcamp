'''
This is a "basic" version of rock-paper-scissors.
It will use input of two users and determine the winner based on the
choice.
This is a simple beginner project that uses boolean logic 
'''

print("...rock...")
print("...paper...")
print("...scissors...")

# The players choose their weapon
player_1 = input("enter Player 1's choice: ")
player_2 = input("enter Player 2's choice: ")

'''
Instead of checking *all* possibilites we only check where Player 1 wins.
If Player 1 does not win, it's either a draw or a win for player 2.
This makes the code more efficient.
'''
if player_1 == player_2:
    print("It's a draw!")
elif player_1 == "rock" and player_2 == "scissors":
    print("Player 1 wins!")
elif player_1 == "paper" and player_2 == "rock":
    print("Player 1 wins!")
elif player_1 == "scissors" and player_2 == "paper":
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
