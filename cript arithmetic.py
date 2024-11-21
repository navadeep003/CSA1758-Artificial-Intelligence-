from itertools import permutations

def solve_cryptarithmetic(word1, word2, result):
    """Solve cryptarithmetic problems where word1 + word2 = result."""
    # Create a set of unique letters
    unique_letters = set(word1 + word2 + result)
    
    # Ensure there are not more than 10 unique letters
    if len(unique_letters) > 10:
        raise ValueError("Too many unique letters! Maximum is 10.")
    
    # Convert the words to lists of letters
    word1, word2, result = list(word1), list(word2), list(result)
    
    # Try all permutations of digits (0-9) of length equal to unique letters
    for perm in permutations(range(10), len(unique_letters)):
        # Map each letter to a digit
        char_to_digit = dict(zip(unique_letters, perm))
        
        # Ensure no number starts with zero
        if char_to_digit[word1[0]] == 0 or char_to_digit[word2[0]] == 0 or char_to_digit[result[0]] == 0:
            continue
        
        # Convert the words to numbers
        num1 = int("".join(str(char_to_digit[char]) for char in word1))
        num2 = int("".join(str(char_to_digit[char]) for char in word2))
        num_result = int("".join(str(char_to_digit[char]) for char in result))
        
        # Check if the equation is satisfied
        if num1 + num2 == num_result:
            return num1, num2, num_result, char_to_digit  # Return numbers and mapping
    
    return None  # If no solution is found


# User Input
print("Welcome to the Cryptarithmetic Solver!")
word1 = input("Enter the first word (e.g., SEND): ").strip().upper()
word2 = input("Enter the second word (e.g., MORE): ").strip().upper()
result = input("Enter the result word (e.g., MONEY): ").strip().upper()

# Solve the problem
try:
    solution = solve_cryptarithmetic(word1, word2, result)
    if solution:
        num1, num2, num_result, mapping = solution
        print("\nSolution found!")
        print(f"{word1} = {num1}")
        print(f"{word2} = {num2}")
        print(f"{result} = {num_result}")
        print(f"Addition: {num1} + {num2} = {num_result}")
        print("\nLetter to digit mapping:")
        for char, digit in mapping.items():
            print(f"{char} = {digit}")
    else:
        print("\nNo solution exists.")
except ValueError as e:
    print(f"\nError: {e}")
