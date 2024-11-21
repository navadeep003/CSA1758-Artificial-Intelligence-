def dfs(graph, start_node, visited=None, traversal_order=None):
    """Performs DFS on the given graph from the start_node."""
    if visited is None:
        visited = set()  # To keep track of visited nodes
    if traversal_order is None:
        traversal_order = []  # List to store the order of traversal

    visited.add(start_node)
    traversal_order.append(start_node)

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal_order)

    return traversal_order

def main():
    print("Welcome to the DFS Traversal Program!")

    # Input the graph
    n = int(input("Enter the number of nodes in the graph: "))
    print("Enter the adjacency list for the graph:")
    graph = {}
    for _ in range(n):
        node, *neighbors = input("Node and its neighbors (space-separated): ").split()
        graph[node] = neighbors

    # Input the starting node
    start_node = input("Enter the starting node: ")

    if start_node not in graph:
        print(f"Error: Starting node '{start_node}' is not in the graph.")
        return

    # Perform DFS
    print("\nPerforming DFS...")
    traversal_order = dfs(graph, start_node)

    # Output the result
    print("\nDFS Traversal Order:")
    print(" -> ".join(traversal_order))

if __name__ == "__main__":
    main()
