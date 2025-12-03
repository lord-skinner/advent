# Define constants
input_file = "input.txt"

# Read input from the file
with open(input_file, "r") as f:
    raw_data = f.read()

# Split the input into a grid of characters
grid = raw_data.split("\n")
height = len(grid)
width = len(grid[0])

# Initialize a grid to mark enclosed tiles
enclosed_grid = [[0] * width for _ in range(height)]

# Find the starting position 'S'
start_x, start_y = -1, -1
for i in range(height):
    if "S" in grid[i]:
        start_x = i
        start_y = grid[i].find("S")
        break


# Define possible movement directions: right, down, left, up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
valid_pipes = ["-7J", "|LJ", "-FL", "|F7"]
start_directions = []

# Determine valid directions from the starting position
for i in range(4):
    dx, dy = directions[i]
    new_x = start_x + dx
    new_y = start_y + dy
    
    # Check if the new position is within bounds and valid
    if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] in valid_pipes[i]:
        start_directions.append(i)

is_valid_start = 3 in start_directions  # Check if downward direction is valid

# Define transformation rules for direction changes based on pipe type
transformations = {
    (0, "-"): 0,
    (0, "7"): 1,
    (0, "J"): 3,
    (2, "-"): 2,
    (2, "F"): 1,
    (2, "L"): 3,
    (1, "|"): 1,
    (1, "L"): 0,
    (1, "J"): 2,
    (3, "|"): 3,
    (3, "F"): 0,
    (3, "7"): 2,
}

# Start navigating through the loop from 'S'
current_direction = start_directions[0]
current_x = start_x + directions[current_direction][0]
current_y = start_y + directions[current_direction][1]
length_of_path = 1

# Mark starting position as part of the loop
enclosed_grid[start_x][start_y] = 1

# Traverse the loop until returning to starting position
while (current_x, current_y) != (start_x, start_y):
    enclosed_grid[current_x][current_y] = 1  # Mark this tile as part of the loop
    length_of_path += 1
    
    # Update direction based on current tile type
    current_direction = transformations[(current_direction, grid[current_x][current_y])]
    
    # Move to the next tile in the current direction
    current_x += directions[current_direction][0]
    current_y += directions[current_direction][1]

print(f"Half of path length: {length_of_path // 2}")

# Count enclosed tiles based on marked loop tiles
count_enclosed_tiles = 0
for i in range(height):
    inside_loop = False
    for j in range(width):
        if enclosed_grid[i][j]:  # If this tile is part of the loop
            if grid[i][j] in "|JL" or (grid[i][j] == "S" and is_valid_start):
                inside_loop = not inside_loop  # Toggle inside/outside status
        else:
            count_enclosed_tiles += inside_loop  # Count enclosed tiles

print(f"Number of enclosed tiles: {count_enclosed_tiles}")