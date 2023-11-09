import tkinter as tk
import random

def determine_winner(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Scissors" and computer_choice == "Paper")
        or (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result_label.config(text=f"You chose {user_choice} and\nComputer chose {computer_choice}. You win!")
    else:
        result_label.config(text=f"You chose {user_choice} and\nComputer chose {computer_choice}. Computer wins!")

def button_click(choice):
    determine_winner(choice)
    
window = tk.Tk()
window.title("Rock, Paper, Scissors")
rock_button = tk.Button(window, text="Rock", command=lambda: button_click("Rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: button_click("Paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: button_click("Scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()
