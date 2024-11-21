import heapq

class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0, cost=0):
        self.state = state  # Current state of the puzzle
        self.parent = parent  # Parent node in the solution path
        self.move = move  # Move made to reach this state
        self.depth = depth  # Depth of the node in the search tree
        self.cost = cost  # Cost = depth + heuristic

    def __lt__(self, other):
        return self.cost < other.cost

# Define goal state
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Heuristic function: Manhattan distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Skip the blank tile
                goal_x, goal_y = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Generate child states by moving the blank tile
def generate_children(node):
    state = node.state
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)  # Find blank tile
    moves = []
    directions = {
        "UP": (-1, 0), "DOWN": (1, 0),
        "LEFT": (0, -1), "RIGHT": (0, 1)
    }
    for move, (dx, dy) in directions.items():
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]  # Create a deep copy
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            moves.append(Puzzle(new_state, node, move, node.depth + 1))
    return moves

# Check if the puzzle is solvable
def is_solvable(state):
    flat = [num for row in state for num in row if num != 0]
    inversions = sum(1 for i in range(len(flat)) for j in range(i + 1, len(flat)) if flat[i] > flat[j])
    zero_row = next(i for i in range(3) if 0 in state[i])
    # Add row index to inversion count for solvability check
    return (inversions + zero_row) % 2 == 0

# Solve the puzzle using A* search
def solve_puzzle(start_state):
    if not is_solvable(start_state):
        return None, "The puzzle is not solvable."

    start_node = Puzzle(start_state, cost=manhattan_distance(start_state))
    frontier = []
    heapq.heappush(frontier, start_node)
    explored = set()

    while frontier:
        current = heapq.heappop(frontier)
        explored.add(tuple(tuple(row) for row in current.state))

        if current.state == GOAL_STATE:
            return current, None

        for child in generate_children(current):
            child.cost = child.depth + manhattan_distance(child.state)
            if tuple(tuple(row) for row in child.state) not in explored:
                heapq.heappush(frontier, child)

    return None, "No solution found."

# Print the solution path
def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    path.reverse()

    print("Solution Steps:")
    total_cost = 0
    for step, node in enumerate(path):
        print(f"Step {step}: Move {node.move} | Cost: {node.depth}")
        total_cost = node.depth
        for row in node.state:
            print(row)
        print()
    print(f"Total Cost: {total_cost}")

# Main function
def main():
    print("Enter the 8-puzzle initial state row by row (use 0 for the blank):")
    start_state = [list(map(int, input(f"Row {i + 1}: ").split())) for i in range(3)]

    print("\nSolving the puzzle...")
    solution, error = solve_puzzle(start_state)

    if solution:
        print_solution(solution)
    else:
        print(error)

if __name__ == "__main__":
    main()
