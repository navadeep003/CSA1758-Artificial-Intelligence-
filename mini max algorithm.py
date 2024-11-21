import math

def print_board(board):
    """Prints the current state of the board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def is_winner(board, player):
    """Check if the given player has won."""
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)

def get_valid_moves(board):
    """Returns a list of valid moves (row, col) on the board."""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing, alpha, beta):
    """Minimax algorithm with alpha-beta pruning."""
    if is_winner(board, "O"):  # AI wins
        return 10 - depth
    if is_winner(board, "X"):  # Human wins
        return depth - 10
    if is_full(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row, col in get_valid_moves(board):
            board[row][col] = "O"
            score = minimax(board, depth + 1, False, alpha, beta)
            board[row][col] = " "
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for row, col in get_valid_moves(board):
            board[row][col] = "X"
            score = minimax(board, depth + 1, True, alpha, beta)
            board[row][col] = " "
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def find_best_move(board):
    """Find the best move for the AI using Minimax."""
    best_score = -math.inf
    best_move = None
    for row, col in get_valid_moves(board):
        board[row][col] = "O"
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[row][col] = " "
        if score > best_score:
            best_score = score
            best_move = (row, col)
    return best_move

def main():
    print("Welcome to Tic Tac Toe with AI!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    print("You are 'X', and the AI is 'O'.")
    print("Enter your moves as row and column numbers (1-3).")

    while True:
        # Human's turn
        while True:
            try:
                move = input("Enter your move (row and column): ")
                row, col = map(int, move.split())
                if board[row - 1][col - 1] == " ":
                    board[row - 1][col - 1] = "X"
                    break
                else:
                    print("Cell already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as numbers between 1 and 3.")

        print_board(board)

        if is_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI's turn
        print("AI is making its move...")
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"
        print_board(board)

        if is_winner(board, "O"):
            print("AI wins! Better luck next time!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
