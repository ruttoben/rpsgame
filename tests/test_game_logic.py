import game_logic


def test_determine_winner_draw():
    assert game_logic.determine_winner("rock", "rock") == 0


def test_determine_winner_player1_wins():
    assert game_logic.determine_winner("rock", "scissors") == 1
    assert game_logic.determine_winner("paper", "rock") == 1
    assert game_logic.determine_winner("scissors", "paper") == 1


def test_determine_winner_player2_wins():
    assert game_logic.determine_winner("rock", "paper") == 2
    assert game_logic.determine_winner("paper", "scissors") == 2
    assert game_logic.determine_winner("scissors", "rock") == 2


def test_get_computer_choice_valid():
    # Ensure the random choice is one of the allowed options
    assert game_logic.get_computer_choice() in game_logic.choices
