import tkinter as tk
import random

class RPSGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")
        self.master.geometry("350x400")
        self.master.resizable(False, False)

        self.score_to_win = 5
        self.user_score = 0
        self.computer_score = 0

        # Title
        self.title_label = tk.Label(master, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Scores display
        self.score_label = tk.Label(master, text=self.get_score_text(), font=("Arial", 14))
        self.score_label.pack(pady=5)

        # Buttons for moves
        self.btn_frame = tk.Frame(master)
        self.btn_frame.pack(pady=10)

        self.btn_rock = tk.Button(self.btn_frame, text="Rock", width=12, command=lambda: self.game_result("rock"))
        self.btn_rock.grid(row=0, column=0, padx=5)

        self.btn_paper = tk.Button(self.btn_frame, text="Paper", width=12, command=lambda: self.game_result("paper"))
        self.btn_paper.grid(row=0, column=1, padx=5)

        self.btn_scissors = tk.Button(self.btn_frame, text="Scissors", width=12, command=lambda: self.game_result("scissors"))
        self.btn_scissors.grid(row=0, column=2, padx=5)

        # Output label
        self.output_label = tk.Label(master, text="", font=("Arial", 12), justify="center", height=5)
        self.output_label.pack(pady=15)

        # Frame for post-game buttons (initially hidden)
        self.post_game_frame = tk.Frame(master)
        self.post_game_frame.pack(pady=10)

        self.restart_btn = tk.Button(self.post_game_frame, text="Restart", width=12, command=self.restart_game)
        self.continue_btn = tk.Button(self.post_game_frame, text="Continue (+5 to win)", width=16, command=self.continue_game)
        self.close_btn = tk.Button(self.post_game_frame, text="Close", width=12, command=master.destroy)

        # Hide post-game buttons initially
        self.post_game_frame.pack_forget()

    def get_score_text(self):
        return f"Score to Win: {self.score_to_win} | You: {self.user_score}  Computer: {self.computer_score}"

    def decide_winner(self, user, comp):
        if user == comp:
            return "draw"
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            return "win"
        else:
            return "lose"

    def game_result(self, user_move):
        if self.user_score >= self.score_to_win or self.computer_score >= self.score_to_win:
            # Prevent playing after game is over, until restart/continue
            return

        choices = ["rock", "paper", "scissors"]
        computer_move = random.choice(choices)
        result = self.decide_winner(user_move, computer_move)

        if result == "win":
            self.user_score += 1
            result_text = "You win this round!"
        elif result == "lose":
            self.computer_score += 1
            result_text = "Computer wins this round!"
        else:
            result_text = "It's a draw!"

        self.score_label.config(text=self.get_score_text())
        self.output_label.config(
            text=f"You chose: {user_move}\nComputer chose: {computer_move}\n{result_text}"
        )

        if self.user_score >= self.score_to_win or self.computer_score >= self.score_to_win:
            self.end_game()

    def end_game(self):
        if self.user_score >= self.score_to_win:
            final_msg = f"You won the game with {self.user_score} points!"
        else:
            final_msg = f"Computer won the game with {self.computer_score} points!"
        
        self.output_label.config(text=final_msg + "\n\nChoose Restart, Continue, or Close.")

        # Disable move buttons
        self.btn_rock.config(state=tk.DISABLED)
        self.btn_paper.config(state=tk.DISABLED)
        self.btn_scissors.config(state=tk.DISABLED)

        # Show post-game buttons
        self.post_game_frame.pack(pady=10)
        self.restart_btn.grid(row=0, column=0, padx=5)
        self.continue_btn.grid(row=0, column=1, padx=5)
        self.close_btn.grid(row=0, column=2, padx=5)

    def restart_game(self):
        # Reset scores and score_to_win to default 5
        self.score_to_win = 5
        self.user_score = 0
        self.computer_score = 0
        self.update_game_state()

    def continue_game(self):
        # Increase the score to win by 5 and reset scores
        self.score_to_win += 5
        self.user_score = 0
        self.computer_score = 0
        self.update_game_state()

    def update_game_state(self):
        # Enable buttons
        self.btn_rock.config(state=tk.NORMAL)
        self.btn_paper.config(state=tk.NORMAL)
        self.btn_scissors.config(state=tk.NORMAL)

        # Update labels
        self.score_label.config(text=self.get_score_text())
        self.output_label.config(text="Game restarted. Make your move!")

        # Hide post-game buttons
        self.post_game_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()
