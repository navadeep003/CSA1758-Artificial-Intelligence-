import math

# Alpha-Beta Pruning Function
def alpha_beta_pruning(depth, node_index, is_maximizing, scores, alpha, beta):
    # Base case: If we reach a leaf node
    if depth == 0 or node_index >= len(scores):
        return scores[node_index]

    if is_maximizing:
        max_eval = -math.inf
        for i in range(2):  # Each node has 2 children
            eval_value = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, scores, alpha, beta)
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):  # Each node has 2 children
            eval_value = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, scores, alpha, beta)
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Main Function
def main():
    print("Alpha-Beta Pruning Algorithm")

    # User input for depth of the tree
    max_depth = int(input("Enter the depth of the game tree: "))
    num_leaves = 2 ** max_depth  # Number of leaf nodes

    # User input for leaf node scores
    print(f"Enter the scores for the {num_leaves} leaf nodes (space-separated):")
    scores = list(map(int, input().split()))

    if len(scores) != num_leaves:
        print(f"Error: You need to provide exactly {num_leaves} scores.")
        return

    # Alpha-Beta Pruning Execution
    print("\nStarting Alpha-Beta Pruning...")
    result = alpha_beta_pruning(max_depth, 0, True, scores, -math.inf, math.inf)
    print("\nOptimal value obtained:", result)

# Run the main function
if __name__ == "__main__":
    main()
