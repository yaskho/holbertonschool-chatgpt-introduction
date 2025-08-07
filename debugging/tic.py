#!/usr/bin/python3

def print_board(board):
    """Prints the current state of the game board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")


def check_winner(board):
    """Checks if there is a winner on the board."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_board_full(board):
    """Returns True if the board is full (draw), else False."""
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Get user input with validation
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")
            continue

        # Check for valid coordinates
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("❌ Invalid position. Please enter 0, 1, or 2.")
            continue

        # Check if the cell is already taken
        if board[row][col] != " ":
            print("❌ That spot is already taken. Try again.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
