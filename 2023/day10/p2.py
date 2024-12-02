from collections import deque

# Read input from the file and split it into lines
with open("./input.txt") as fin:
    lines = fin.read().strip().split("\n")

# Get dimensions of the grid
num_rows = len(lines)
num_cols = len(lines[0])

def get_neighbors(row, col):
    """Return valid neighboring positions for a given tile."""
    neighbors = []
    for delta_row, delta_col in get_directions(row, col):
        new_row, new_col = row + delta_row, col + delta_col
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            neighbors.append((new_row, new_col))
    return neighbors

def get_directions(row, col):
    """Return possible directions based on the type of pipe at (row, col)."""
    if lines[row][col] == "S":
        directions = []
        for delta_row, delta_col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                if (row, col) in get_neighbors(new_row, new_col):
                    directions.append((delta_row, delta_col))
        return directions

    pipe_connections = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, 1), (0, -1)],
        "L": [(-1, 0), (0, 1)],
        "J": [(-1, 0), (0, -1)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        ".": [],
    }
    
    return pipe_connections[lines[row][col]]

# Find the starting position 'S'
start_row, start_col = None, None
for row_index in range(num_rows):
    if "S" in lines[row_index]:
        start_row = row_index
        start_col = lines[row_index].index("S")
        break

# Perform BFS to find all tiles in the loop
loop_tiles = set()
visited = set()
queue = deque([(start_row, start_col)])  # Start BFS from 'S'

while queue:
    current_position = queue.popleft()
    
    if current_position in visited:
        continue
    
    visited.add(current_position)
    
    # Check if it's part of the loop
    row, col = current_position
    if lines[row][col] != ".":  
        loop_tiles.add(current_position)

    for neighbor in get_neighbors(row, col):
        if neighbor not in visited:
            queue.append(neighbor)

# Flood fill to mark outside area
def flood_fill(row, col):
    """Mark all reachable tiles from (row,col) as outside."""
    outside_queue = deque([(row, col)])
    
    while outside_queue:
        current = outside_queue.popleft()
        
        # If it's already visited or part of the loop or out of bounds
        if current in visited or current in loop_tiles:
            continue
        
        visited.add(current)

        for neighbor in get_neighbors(*current):
            if neighbor not in visited:
                outside_queue.append(neighbor)

# Start flood fill from all edges that are ground tiles '.'
for r in range(num_rows):
    for c in range(num_cols):
        # Start flood fill from any outer edge tile that is not a pipe
        if (r == 0 or r == num_rows - 1 or c == 0 or c == num_cols - 1) and lines[r][c] == ".":
            flood_fill(r, c)

# Count enclosed tiles
enclosed_tiles_count = sum(1 for r in range(num_rows) for c in range(num_cols)
                            if lines[r][c] == "." and (r,c) not in visited and (r,c) not in loop_tiles)

print(f"The number of enclosed tiles is: {enclosed_tiles_count}")