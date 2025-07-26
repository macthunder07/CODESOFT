import tkinter as tk
import random

def game_result(user_move):
    choices = ["rock", "paper", "scissors"]
    computer_move = random.choice(choices)
    result = decide_winner(user_move, computer_move)
    output_label.config(
        text=f"You chose: {user_move}\nComputer chose: {computer_move}\n{result}"
    )

def decide_winner(user, comp):
    if user == comp:
        return "It's a draw!"
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        return "You win!"
    else:
        return "You lose!"


window = tk.Tk()
window.title("RPS Game")
window.geometry("300x300")


tk.Button(window, text="Rock", width=12, command=lambda: game_result("rock")).pack(pady=5)
tk.Button(window, text="Paper", width=12, command=lambda: game_result("paper")).pack(pady=5)
tk.Button(window, text="Scissors", width=12, command=lambda: game_result("scissors")).pack(pady=5)


output_label = tk.Label(window, text="", font=("Arial", 12))
output_label.pack(pady=20)


window.mainloop()
