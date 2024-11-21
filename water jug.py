from collections import deque

def water_jug_solver(jug1_capacity, jug2_capacity, target):
    """Solve the water jug problem using BFS."""
    # BFS queue to store the current state (jug1, jug2) and the path
    queue = deque([(0, 0)])  # Start with both jugs empty
    visited = set()  # To avoid revisiting states
    path = {}  # Store parent states for reconstructing the solution

    # Helper to reconstruct the path
    def get_path(state):
        result = []
        while state is not None:
            result.append(state)
            state = path.get(state)
        return result[::-1]

    # BFS
    while queue:
        jug1, jug2 = queue.popleft()

        # Check if we've reached the target
        if jug1 == target or jug2 == target:
            solution_path = get_path((jug1, jug2))
            return solution_path

        # Mark the current state as visited
        visited.add((jug1, jug2))

        # Generate all possible moves
        moves = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            (max(jug1 - (jug2_capacity - jug2), 0),  # Pour jug1 -> jug2
             min(jug2 + jug1, jug2_capacity)),
            (min(jug1 + jug2, jug1_capacity),        # Pour jug2 -> jug1
             max(jug2 - (jug1_capacity - jug1), 0))
        ]

        # Enqueue valid moves
        for new_state in moves:
            if new_state not in visited:
                queue.append(new_state)
                path[new_state] = (jug1, jug2)

    return None  # No solution found

def main():
    print("Welcome to the Water Jug Problem Solver!")
    jug1_capacity = int(input("Enter the capacity of Jug 1: "))
    jug2_capacity = int(input("Enter the capacity of Jug 2: "))
    target = int(input("Enter the target amount of water: "))

    if target > max(jug1_capacity, jug2_capacity):
        print("The target amount cannot be larger than the capacity of either jug.")
        return

    solution = water_jug_solver(jug1_capacity, jug2_capacity, target)

    if solution:
        print("\nSolution Path:")
        for step, (jug1, jug2) in enumerate(solution):
            print(f"Step {step}: Jug1 = {jug1}, Jug2 = {jug2}")
    else:
        print("\nNo solution exists for the given problem.")

if __name__ == "__main__":
    main()
