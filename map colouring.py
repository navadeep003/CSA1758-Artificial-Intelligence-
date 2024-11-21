def is_valid_coloring(node, color, graph, colors):
    """Check if the current color assignment is valid."""
    for neighbor in graph.get(node, []):
        if colors[neighbor] == color:  # Check adjacent nodes
            return False
    return True

def map_coloring_backtracking(graph, num_colors, colors, node_list, index=0):
    """Solve the map coloring problem using backtracking."""
    if index == len(node_list):  # All nodes are colored
        return True

    current_node = node_list[index]
    for color in range(1, num_colors + 1):
        if is_valid_coloring(current_node, color, graph, colors):
            colors[current_node] = color  # Assign the color
            if map_coloring_backtracking(graph, num_colors, colors, node_list, index + 1):
                return True
            colors[current_node] = 0  # Backtrack

    return False

def main():
    print("Welcome to the Map Coloring Problem Solver!")

    # Input the graph
    num_regions = int(input("Enter the number of regions on the map: "))
    print("Enter the adjacency list for the map:")
    graph = {}
    for _ in range(num_regions):
        line = input("Region and neighbors (space-separated): ").split()
        region = line[0]
        neighbors = line[1:]
        graph[region] = neighbors

    # Input the number of colors
    num_colors = int(input("Enter the number of available colors: "))
    if num_colors <= 0:
        print("Error: Number of colors must be greater than 0.")
        return

    # Prepare for backtracking
    colors = {region: 0 for region in graph}  # Color assignment (0 = uncolored)
    node_list = list(graph.keys())

    print("\nSolving the Map Coloring Problem...")
    if map_coloring_backtracking(graph, num_colors, colors, node_list):
        print("\nSolution Found!")
        for region, color in colors.items():
            print(f"Region {region}: Color {color}")
    else:
        print("\nNo solution exists with the given number of colors.")

if __name__ == "__main__":
    main()
