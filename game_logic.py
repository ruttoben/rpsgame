import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    """Randomly returns 'rock', 'paper', or 'scissors'."""
    return random.choice(choices)

def determine_winner(player1, player2):
    """Returns 0 if draw, 1 if player1 wins, 2 if player2 wins."""
    if player1 == player2:
        return 0
    elif (
        (player1 == "rock" and player2 == "scissors") or
        (player1 == "scissors" and player2 == "paper") or
        (player1 == "paper" and player2 == "rock")
    ):
        return 1
    else:
        return 2