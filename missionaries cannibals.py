from collections import deque

def is_valid_state(state, boat_capacity):
    """Check if the current state is valid."""
    m_left, c_left, m_right, c_right, boat = state

    # Ensure no side has more cannibals than missionaries (unless zero missionaries)
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False

    # Ensure the state is within valid bounds
    if not (0 <= m_left <= 3 and 0 <= c_left <= 3 and 0 <= m_right <= 3 and 0 <= c_right <= 3):
        return False

    return True

def generate_successors(state, boat_capacity):
    """Generate all possible successors from the current state."""
    m_left, c_left, m_right, c_right, boat = state
    successors = []
    if boat == "left":  # Boat is on the left side
        for m in range(boat_capacity + 1):
            for c in range(boat_capacity + 1 - m):
                if m + c >= 1:  # At least one person must cross
                    new_state = (m_left - m, c_left - c, m_right + m, c_right + c, "right")
                    if is_valid_state(new_state, boat_capacity):
                        successors.append(new_state)
    else:  # Boat is on the right side
        for m in range(boat_capacity + 1):
            for c in range(boat_capacity + 1 - m):
                if m + c >= 1:  # At least one person must cross
                    new_state = (m_left + m, c_left + c, m_right - m, c_right - c, "left")
                    if is_valid_state(new_state, boat_capacity):
                        successors.append(new_state)
    return successors

def solve_missionaries_cannibals(boat_capacity):
    """Solve the Missionaries and Cannibals Problem using BFS."""
    initial_state = (3, 3, 0, 0, "left")  # (Missionaries_left, Cannibals_left, Missionaries_right, Cannibals_right, Boat)
    goal_state = (0, 0, 3, 3, "right")

    queue = deque([initial_state])
    visited = set()
    parent = {initial_state: None}

    while queue:
        current_state = queue.popleft()

        # Check if the goal state is reached
        if current_state[:4] == goal_state[:4]:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent[current_state]
            return path[::-1]

        visited.add(current_state)

        # Generate all valid successors
        for successor in generate_successors(current_state, boat_capacity):
            if successor not in visited and successor not in queue:
                queue.append(successor)
                parent[successor] = current_state

    return None  # No solution found

def print_solution(path):
    """Print the solution path."""
    if not path:
        print("\nNo solution exists.")
        return

    print("\nSolution Path:")
    for step, state in enumerate(path):
        m_left, c_left, m_right, c_right, boat = state
        print(f"Step {step}:")
        print(f"Left Bank: Missionaries = {m_left}, Cannibals = {c_left}")
        print(f"Right Bank: Missionaries = {m_right}, Cannibals = {c_right}")
        print(f"Boat is on the {boat} bank.\n")

def main():
    print("Welcome to the Missionaries and Cannibals Problem Solver!")
    boat_capacity = int(input("Enter the boat capacity (recommended: 2): "))
    if boat_capacity < 1:
        print("Boat capacity must be at least 1.")
        return

    print("\nSolving the problem...")
    solution = solve_missionaries_cannibals(boat_capacity)

    print_solution(solution)

if __name__ == "__main__":
    main()
