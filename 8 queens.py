def print_board(board):
    """Print the chessboard with queens placed."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check column above
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row, n):
    """Solve the N Queens problem using backtracking."""
    if row == n:
        print_board(board)  # Print solution
        return True  # Return True if a solution is found

    found_solution = False
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 1
            # Recursively solve for the next row
            found_solution = solve_n_queens(board, row + 1, n) or found_solution
            # Backtrack
            board[row][col] = 0

    return found_solution

def main():
    print("Welcome to the N-Queens Problem Solver!")
    n = int(input("Enter the size of the board (N): "))
    if n < 4:
        print("There are no solutions for N < 4. Please try again with N >= 4.")
        return

    board = [[0 for _ in range(n)] for _ in range(n)]
    print(f"\nSolutions for the {n}-Queens Problem:\n")
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")

if __name__ == "__main__":
    main()
