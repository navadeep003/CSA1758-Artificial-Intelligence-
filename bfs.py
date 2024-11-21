from collections import deque

def bfs(graph, start_node):
    """Performs BFS on the given graph from the start_node."""
    visited = set()  # To keep track of visited nodes
    queue = deque([start_node])  # Queue for BFS
    traversal_order = []  # List to store the order of traversal

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)

            # Add unvisited neighbors to the queue
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

def main():
    print("Welcome to the BFS Traversal Program!")

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

    # Perform BFS
    print("\nPerforming BFS...")
    traversal_order = bfs(graph, start_node)

    # Output the result
    print("\nBFS Traversal Order:")
    print(" -> ".join(traversal_order))

if __name__ == "__main__":
    main()
