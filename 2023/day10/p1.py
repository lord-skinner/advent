from collections import deque

# Read input from the file and split it into lines
with open("./input.txt") as fin:
    lines = fin.read().strip().split("\n")

# Get the dimensions of the grid
num_rows = len(lines)
num_cols = len(lines[0])

def get_neighbors(row, col):
    """Return valid neighboring positions for a given tile."""
    neighbors = []
    # Check all possible directions based on the current tile type
    for delta_row, delta_col in get_directions(row, col):
        new_row, new_col = row + delta_row, col + delta_col
        # Ensure the new position is within grid bounds
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            neighbors.append((new_row, new_col))
    return neighbors

def get_directions(row, col):
    """Return possible directions based on the type of pipe at (row, col)."""
    # If it's the starting position 'S', check connections to neighbors
    if lines[row][col] == "S":
        directions = []
        for delta_row, delta_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Check if the neighbor can connect back to 'S'
                if (row, col) in get_neighbors(new_row, new_col):
                    directions.append((delta_row, delta_col))
        return directions

    # Define connections based on pipe types
    pipe_connections = {
        "|": [(1, 0), (-1, 0)],  # Vertical pipes connect up and down
        "-": [(0, 1), (0, -1)],  # Horizontal pipes connect left and right
        "L": [(-1, 0), (0, 1)],  # L-bend connects up and right
        "J": [(-1, 0), (0, -1)], # J-bend connects up and left
        "7": [(1, 0), (0, -1)],  # 7-bend connects down and left
        "F": [(1, 0), (0, 1)],   # F-bend connects down and right
        ".": [],                 # Ground has no connections
    }
    
    return pipe_connections[lines[row][col]]

# Find the starting position 'S'
start_row, start_col = None, None
for row_index, line in enumerate(lines):
    if "S" in line:
        start_row = row_index
        start_col = line.index("S")
        break

# Perform a breadth-first search (BFS) to find distances from 'S'
visited = set()           # Set to track visited positions
distances = {}           # Dictionary to store distances from 'S'
queue = deque([((start_row, start_col), 0)])  # Queue for BFS

while queue:
    current_position, current_distance = queue.popleft()
    
    if current_position in visited:
        continue
    
    visited.add(current_position)
    distances[current_position] = current_distance

    for neighbor in get_neighbors(*current_position):
        if neighbor not in visited:
            queue.append((neighbor, current_distance + 1))

# Find the maximum distance from the starting position 'S'
max_distance = max(distances.values())
print(max_distance)