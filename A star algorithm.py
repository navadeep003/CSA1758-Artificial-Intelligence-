import heapq

def a_star_algorithm(graph, start, goal, heuristic):
    """
    A* Algorithm to find the shortest path from start to goal.
    :param graph: A dictionary where keys are nodes and values are dictionaries of neighbors and their costs.
    :param start: Starting node.
    :param goal: Goal node.
    :param heuristic: A dictionary of heuristic values for each node.
    :return: Shortest path and its cost.
    """
    open_list = []  # Priority queue
    heapq.heappush(open_list, (0, start))  # (cost, node)
    came_from = {}  # Tracks the path
    g_score = {node: float('inf') for node in graph}  # Cost from start to each node
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  # Estimated total cost
    f_score[start] = heuristic[start]

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        # If we reach the goal
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        # Process neighbors
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None, float('inf')  # No path found

def main():
    print("Welcome to the A* Algorithm Solver!")

    # Input the graph
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    print("Enter the graph as adjacency lists with weights:")
    graph = {}
    for _ in range(num_nodes):
        line = input("Node and neighbors (e.g., A B:1 C:4): ").split()
        node = line[0]
        neighbors = {}
        for neighbor_cost in line[1:]:
            neighbor, cost = neighbor_cost.split(':')
            neighbors[neighbor] = int(cost)
        graph[node] = neighbors

    # Input the heuristic values
    print("\nEnter the heuristic values for each node:")
    heuristic = {}
    for _ in range(num_nodes):
        node, h_value = input("Node and heuristic value (e.g., A 5): ").split()
        heuristic[node] = int(h_value)

    # Input the start and goal nodes
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    if start not in graph or goal not in graph:
        print("Error: Start or goal node is not in the graph.")
        return

    print("\nRunning A* Algorithm...")
    path, cost = a_star_algorithm(graph, start, goal, heuristic)

    # Output the result
    if path:
        print("\nShortest Path:")
        print(" -> ".join(path))
        print(f"Total Cost: {cost}")
    else:
        print("No path found from start to goal.")

if __name__ == "__main__":
    main()
