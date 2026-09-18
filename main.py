# literally just need a file to put out -  James
import tkinter as tk


def check_winner():
	for first, second, third in winning_lines:
		if board[first] and board[first] == board[second] == board[third]:
			return board[first]
	return None


def make_move(position):
	global current_player, game_over

	if game_over or board[position]:
		return

	board[position] = current_player
	buttons[position].configure(text=current_player)

	winner = check_winner()
	if winner:
		status.configure(text=f"Player {winner} wins!")
		game_over = True
	elif all(board):
		status.configure(text="It's a tie!")
		game_over = True
	else:
		current_player = "O" if current_player == "X" else "X"
x		status.configure(text=f"Player {current_player}'s turn")


def reset_game():
	global current_player, game_over

	board[:] = ["" for _ in board]
	current_player = "X"
	game_over = False
	for button in buttons:
		button.configure(text="")
	status.configure(text="Player X's turn")


window = tk.Tk()
window.title("Tic-Tac-Toe")

board = ["" for _ in range(9)]
buttons = []
winning_lines = (
	(0, 1, 2),
	(3, 4, 5),
	(6, 7, 8),
	(0, 3, 6),
	(1, 4, 7),
	(2, 5, 8),
	(0, 4, 8),
	(2, 4, 6),
)
current_player = "X"
game_over = False

status = tk.Label(window, text="Player X's turn", font=("Arial", 16))
status.pack(pady=(12, 4))

board_frame = tk.Frame(window)
board_frame.pack(fill="both", expand=True, padx=20, pady=20)

for position in range(9):
	button = tk.Button(
		board_frame,
		font=("Arial", 28, "bold"),
		command=lambda position=position: make_move(position),
	)
	button.grid(
		row=position // 3,
		column=position % 3,
		sticky="nsew",
		padx=3,
		pady=3,
	)
	buttons.append(button)

for index in range(3):
	board_frame.rowconfigure(index, weight=1)
	board_frame.columnconfigure(index, weight=1)

reset_button = tk.Button(window, text="New Game", command=reset_game)
reset_button.pack(pady=(0, 12))

window.mainloop()
