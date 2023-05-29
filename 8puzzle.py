import random
import math

def generate_moves(state):
    """
    Generate all possible moves from the current state.
    """
    moves = []
    empty_index = state.index(0)
    row, col = empty_index // 3, empty_index % 3

    if row > 0:
        moves.append(empty_index - 3)  # Move the tile above the empty space
    if row < 2:
        moves.append(empty_index + 3)  # Move the tile below the empty space
    if col > 0:
        moves.append(empty_index - 1)  # Move the tile to the left of the empty space
    if col < 2:
        moves.append(empty_index + 1)  # Move the tile to the right of the empty space

    return moves

def calculate_heuristic(state, goal_state):
    """
    Calculate the Manhattan distance heuristic between two states.
    """
    distance = 0
    for i in range(len(state)):
        if state[i] != goal_state[i]:
            curr_row, curr_col = i // 3, i % 3
            goal_row, goal_col = goal_state.index(state[i]) // 3, goal_state.index(state[i]) % 3
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

def hill_climbing(initial_state, goal_state):
    """
    Solve the 8-Puzzle Problem using Hill-climbing algorithm.
    """
    current_state = initial_state
    moves_sequence = []

    while current_state != goal_state:
        moves = generate_moves(current_state)
        best_move = None
        best_score = math.inf

        for move in moves:
            new_state = current_state[:]
            new_state[current_state.index(0)], new_state[move] = new_state[move], new_state[current_state.index(0)]
            score = calculate_heuristic(new_state, goal_state)

            if score < best_score:
                best_score = score
                best_move = move

        if best_score >= calculate_heuristic(current_state, goal_state):
            # Stuck in local optima, restart with a new initial state
            current_state = random.sample(range(9), 9)
            moves_sequence = []
        else:
            current_state[current_state.index(0)], current_state[best_move] = current_state[best_move], current_state[current_state.index(0)]
            moves_sequence.append(current_state[:])

    return moves_sequence

# Example usage
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

moves = hill_climbing(initial_state, goal_state)

# Displaying all possible moves
print("Initial state:")
for i in range(0, 9, 3):
    print(initial_state[i:i+3])

print("\nMoves sequence:")
for move in moves:
    for i in range(0, 9, 3):
        print(move[i:i+3])
    print()

print("Goal state:")
for i in range(0, 9, 3):
    print(goal_state[i:i+3])
