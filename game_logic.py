import random

# Valid choices used by both players
choices = ["rock", "paper", "scissors"]


def get_computer_choice():
    """Return a random choice for the computer from `choices`."""
    return random.choice(choices)


def determine_winner(player1, player2):

    if player1 == player2:
        return 0
    # Check winning combinations for player1
    elif (
        (player1 == "rock" and player2 == "scissors") or
        (player1 == "scissors" and player2 == "paper") or
        (player1 == "paper" and player2 == "rock")
    ):
        return 1
    else:
        return 2