from itertools import permutations

def calculate_route_cost(route, distance_matrix):
    """Calculate the total cost of a given route."""
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    cost += distance_matrix[route[-1]][route[0]]  # Return to the starting point
    return cost

def tsp_brute_force(distance_matrix):
    """Solve TSP using brute force."""
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    shortest_route = None
    min_cost = float("inf")

    # Check all permutations of city routes
    for perm in permutations(cities):
        cost = calculate_route_cost(perm, distance_matrix)
        if cost < min_cost:
            min_cost = cost
            shortest_route = perm

    return shortest_route, min_cost

def main():
    print("Welcome to the Traveling Salesman Problem Solver!")

    # Input the number of cities
    num_cities = int(input("Enter the number of cities: "))
    if num_cities < 2:
        print("Error: The number of cities must be at least 2.")
        return

    # Input the distance matrix
    print("Enter the distance matrix (space-separated rows):")
    distance_matrix = []
    for i in range(num_cities):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != num_cities:
            print(f"Error: Row {i + 1} must have exactly {num_cities} elements.")
            return
        distance_matrix.append(row)

    print("\nSolving the TSP...")
    route, cost = tsp_brute_force(distance_matrix)

    # Output the result
    print("\nOptimal Route (0-based indexing):")
    print(" -> ".join(map(str, route)) + f" -> {route[0]}")  # Returning to start
    print(f"Minimum Cost: {cost}")

if __name__ == "__main__":
    main()
