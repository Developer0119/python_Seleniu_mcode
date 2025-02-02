import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize game variables
current_player = "X"
board = [" " for _ in range(9)]  # Represents the 3x3 board

# Function to handle button clicks
def on_click(index):
    global current_player

    # Check if the cell is empty and the game is not over
    if board[index] == " " and not check_winner():
        board[index] = current_player
        buttons[index].config(text=current_player)

        # Check for a winner or a tie
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif " " not in board:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"

# Function to check for a winner
def check_winner():
    # Define winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

# Function to reset the game
def reset_game():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    for button in buttons:
        button.config(text=" ")

# Create buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                       command=lambda i=i: on_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Add a reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 16), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

# Run the main loop
root.mainloop()
