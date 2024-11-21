def print_board(board):
    """Prints the current state of the board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def is_winner(board, player):
    """Check if the given player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)

def get_move(player, board):
    """Prompt the player to make a move."""
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column, 1-3, separated by a space): ")
            row, col = map(int, move.split())
            if board[row - 1][col - 1] == " ":
                return row - 1, col - 1
            else:
                print("The cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as numbers between 1 and 3.")

def main():
    print("Welcome to Tic Tac Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    players = ["X", "O"]
    turn = 0

    while True:
        current_player = players[turn % 2]
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if is_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break
        turn += 1

if __name__ == "__main__":
    main()
