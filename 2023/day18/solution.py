# Read input from the file and split it into a list of commands
plan = list(map(str.split, open('input.txt')))

# Define movement directions as (x, y) coordinate changes
direction_map = {
    'R': (1, 0),   # Right
    'D': (0, 1),   # Down
    'L': (-1, 0),  # Left
    'U': (0, -1),  # Up
    '0': (1, 0),   # Right (alternative representation)
    '1': (0, 1),   # Down (alternative representation)
    '2': (-1, 0),  # Left (alternative representation)
    '3': (0, -1)   # Up (alternative representation)
}

def calculate_position(steps, initial_position=0, initial_answer=1):
    """
    Calculate the final position and answer based on movement steps.

    Parameters:
    - steps: A generator of tuples containing direction vectors and step counts.
    - initial_position: The starting position (default is 0).
    - initial_answer: The starting answer value (default is 1).

    Returns:
    - The final calculated answer as an integer.
    """
    
    current_position = initial_position
    current_answer = initial_answer

    for (x_change, y_change), step_count in steps:
        current_position += x_change * step_count  # Update position based on x change
        current_answer += y_change * step_count * current_position + step_count / 2  # Update answer

    return int(current_answer)  # Return the final answer as an integer

# Calculate results for two different formats of input data
result_part1 = calculate_position((direction_map[direction], int(steps)) for direction, steps, _ in plan)
result_part2 = calculate_position((direction_map[command[7]], int(command[2:7], 16)) for _, _, command in plan)

# Print the results for both parts
print(result_part1, result_part2)