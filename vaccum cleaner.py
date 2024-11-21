from collections import deque

def is_goal_state(room):
    """Check if the room is fully cleaned."""
    for row in room:
        if 1 in row:  # If there is still dirt
            return False
    return True

def get_neighbors(position, room):
    """Get valid neighbors for the vacuum cleaner to move."""
    x, y = position
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(room) and 0 <= ny < len(room[0]):  # Ensure within bounds
            neighbors.append((nx, ny))

    return neighbors

def vacuum_cleaner_solver(room, start):
    """Solve the vacuum cleaner problem using BFS."""
    queue = deque([(start, room, 0, [])])  # (position, current_room_state, steps, path)
    visited = set()

    while queue:
        position, current_room, steps, path = queue.popleft()

        # Mark the current state as visited
        state_signature = (tuple(tuple(row) for row in current_room), position)
        if state_signature in visited:
            continue
        visited.add(state_signature)

        # Check if the room is fully cleaned
        if is_goal_state(current_room):
            return path + [position], steps

        # Clean the current position if dirty
        x, y = position
        if current_room[x][y] == 1:
            current_room = [row[:] for row in current_room]  # Create a new room state
            current_room[x][y] = 0

        # Explore neighbors
        for neighbor in get_neighbors(position, current_room):
            queue.append((neighbor, current_room, steps + 1, path + [position]))

    return None, None  # No solution found

def main():
    print("Welcome to the Vacuum Cleaner Problem Solver!")

    # Get room dimensions
    rows = int(input("Enter the number of rows in the room: "))
    cols = int(input("Enter the number of columns in the room: "))

    # Get the room state
    print("Enter the room state row by row (0 for clean, 1 for dirty):")
    room = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Error: Row {i + 1} must have exactly {cols} elements.")
            return
        room.append(row)

    # Get starting position
    start_x = int(input("Enter the starting X position (row index, 0-based): "))
    start_y = int(input("Enter the starting Y position (column index, 0-based): "))

    if not (0 <= start_x < rows and 0 <= start_y < cols):
        print("Error: Starting position is out of bounds.")
        return

    print("\nSolving the problem...")
    path, steps = vacuum_cleaner_solver(room, (start_x, start_y))

    if path:
        print("\nSolution Found!")
        print("Path to clean the room:")
        for step, pos in enumerate(path):
            print(f"Step {step}: Position {pos}")
        print(f"\nTotal steps taken: {steps}")
    else:
        print("\nNo solution found.")

if __name__ == "__main__":
    main()
