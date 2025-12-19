import tkinter as tk
from tkinter import messagebox
from game_logic import get_computer_choice, determine_winner

#Implements a Tkinter-based GUI for a Rock-Paper-Scissors game, allowing a user to play rounds against the computer, view scores, and reset the game.
class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")

        self.player_score = 0
        self.computer_score = 0

        # Title
        tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold")).pack(pady=10)

        # Score
        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Arial", 12))
        self.score_label.pack(pady=5)

        # Result
        self.result_label = tk.Label(root, text="Make your move!", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        for choice in ["rock", "paper", "scissors"]:
            tk.Button(
                button_frame,
                text=choice.capitalize(),
                width=12,
                command=lambda c=choice: self.play_round(c)
            ).pack(side="left", padx=5)

        # Reset button
        tk.Button(root, text="Reset Game", command=self.reset_game).pack(pady=10)

    def get_score_text(self):
        return f"Player: {self.player_score}  |  Computer: {self.computer_score}"

    def play_round(self, player_choice):
        """
        Handle a single round started by the player selecting `player_choice`.

    - Calls game logic to obtain a randomized computer choice.
    - Determines the round outcome (draw/player/computer).
    - Updates internal scores and the result/score labels shown in the GUI.

    Args:
        player_choice (str): One of "rock", "paper", or "scissors".

    Side effects:
        Mutates `self.player_score` or `self.computer_score` on wins.
        Updates `self.result_label` and `self.score_label`.
    """
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)

        if winner == 0:
            result = "It's a draw!"
        elif winner == 1:
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(
            text=f"You chose {player_choice}\nComputer chose {computer_choice}\n\n{result}"
        )

        self.score_label.config(text=self.get_score_text())

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.result_label.config(text="Make your move!")
        self.score_label.config(text=self.get_score_text())

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    RockPaperScissorsGUI(root)
    root.mainloop()
