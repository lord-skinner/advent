# Read input from the file and create a mapping of complex coordinates to characters
grid = {
    complex(i, j): char 
    for j, row in enumerate(open('input.txt'))
    for i, char in enumerate(row.strip())
}

def process_paths(initial_positions):
    """
    Process paths through the grid based on initial positions and directions.

    Parameters:
    - initial_positions: A list of tuples containing starting positions and directions.

    Returns:
    - The number of unique positions visited minus one.
    """
    visited = set()  # Set to track visited positions and directions
    while initial_positions:
        current_pos, current_dir = initial_positions.pop()
        
        # Continue moving until we revisit a position with the same direction
        while (current_pos, current_dir) not in visited:
            visited.add((current_pos, current_dir))  # Mark the current position and direction as visited
            current_pos += current_dir  # Move in the current direction
            
            # Determine the next direction based on the character at the new position
            match grid.get(current_pos):
                case '|':  # Vertical track
                    current_dir = 1j  # Move down
                    initial_positions.append((current_pos, -current_dir))  # Add reverse direction
                case '-':  # Horizontal track
                    current_dir = -1  # Move left
                    initial_positions.append((current_pos, -current_dir))  # Add reverse direction
                case '/':  # Diagonal track (right)
                    current_dir = -complex(current_dir.imag, current_dir.real)  # Change direction
                case '\\':  # Diagonal track (left)
                    current_dir = complex(current_dir.imag, current_dir.real)  # Change direction
                case None:  # No track (out of bounds)
                    break  # Stop processing this path

    return len(set(pos for pos, _ in visited)) - 1  # Return unique positions minus one

# Start processing from the initial position above the first row
print(process_paths([(-1, 1)]))  # Part 1: Output unique positions visited

# Part 2: Find maximum unique positions visited from all possible starting directions
max_unique_positions = max(
    map(
        process_paths,
        ([(pos - dir, dir)] for dir in (1, 1j, -1, -1j) for pos in grid if pos - dir not in grid)
    )
)

print(max_unique_positions)  # Output maximum unique positions visited across all paths