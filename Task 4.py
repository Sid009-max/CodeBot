import tkinter as tk
import random

# Main window setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")
root.config(bg="black")

user_score = 0
computer_score = 0

# Choices
choices = ["rock", "paper", "scissors"]

# Labels
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), fg="cyan", bg="black")
title_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16), fg="white", bg="black")
result_label.pack(pady=20)

score_label = tk.Label(root, text="You: 0  |  Computer: 0", font=("Arial", 14), fg="yellow", bg="black")
score_label.pack(pady=10)

user_choice_label = tk.Label(root, text="", font=("Arial", 12), fg="lightgreen", bg="black")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="", font=("Arial", 12), fg="lightcoral", bg="black")
computer_choice_label.pack(pady=5)

# Functions
def play(choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"You chose: {choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    if choice == computer_choice:
        result = "It's a Tie!"
        color = "orange"
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        result = "🎉 You Win!"
        user_score += 1
        color = "green"
    else:
        result = "💻 Computer Wins!"
        computer_score += 1
        color = "red"

    result_label.config(text=result, fg=color)
    score_label.config(text=f"You: {user_score}  |  Computer: {computer_score}")

# Buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=30)

rock_btn = tk.Button(button_frame, text="Rock", width=10, height=2, bg="#3498db", fg="white", font=("Arial", 12, "bold"),
                     command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, height=2, bg="#2ecc71", fg="white", font=("Arial", 12, "bold"),
                      command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, height=2, bg="#e74c3c", fg="white", font=("Arial", 12, "bold"),
                         command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Exit button
exit_btn = tk.Button(root, text="Exit", width=10, height=2, bg="#555", fg="white", font=("Arial", 12, "bold"),
                     command=root.destroy)
exit_btn.pack(pady=20)

root.mainloop()
