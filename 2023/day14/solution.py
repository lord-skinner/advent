import sys
from collections import defaultdict

# Read input from file and create a grid representation
with open("input.txt") as file:
    data = file.read().strip()
    grid = [list(row) for row in data.split('\n')]

def rotate(grid):
    """
    Rotate the grid 90 degrees clockwise.
    
    Parameters:
    - grid: 2D list representing the current state of the grid.

    Returns:
    - A new grid that is rotated 90 degrees clockwise.
    """
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [['?' for _ in range(rows)] for _ in range(cols)]
    
    for r in range(rows):
        for c in range(cols):
            new_grid[c][rows - 1 - r] = grid[r][c]
    
    return new_grid

def roll(grid):
    """
    Roll the objects ('O') in the grid upwards if possible.
    
    Parameters:
    - grid: 2D list representing the current state of the grid.

    Returns:
    - The updated grid after rolling.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    for c in range(cols):
        for _ in range(rows):  # Allow multiple rolls
            for r in range(rows):
                if grid[r][c] == 'O' and r > 0 and grid[r - 1][c] == '.':
                    # Move 'O' up if the space above is empty
                    grid[r][c] = '.'  # Clear current position
                    grid[r - 1][c] = 'O'  # Move 'O' up
    
    return grid

def score(grid):
    """
    Calculate the score based on the position of 'O' objects.
    
    Parameters:
    - grid: 2D list representing the current state of the grid.

    Returns:
    - The calculated score as an integer.
    """
    total_score = 0
    rows = len(grid)
    
    for r in range(rows):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                # Score is based on how far down the 'O' is
                total_score += (rows - r)
    
    return total_score

def display_grid(grid):
    """Prints the current state of the grid."""
    for row in grid:
        print(''.join(row))

# Dictionary to track previously seen configurations of the grid
seen_grids = {}

# Set a target number of iterations
target_iterations = 10**9
current_iteration = 0

while current_iteration < target_iterations:
    current_iteration += 1
    
    # Perform rolling and rotating operations
    for _ in range(4):  # Rotate four times (360 degrees)
        grid = roll(grid)  # Roll objects upwards
        
        if current_iteration == 1 and _ == 0:
            print(score(grid))  # Part 1: Print score after first iteration
        
        grid = rotate(grid)  # Rotate the grid
    
    # Convert the current grid to a tuple to use as a dictionary key
    grid_tuple = tuple(tuple(row) for row in grid)
    
    if grid_tuple in seen_grids:
        cycle_length = current_iteration - seen_grids[grid_tuple]
        remaining_iterations = (target_iterations - current_iteration) // cycle_length
        current_iteration += remaining_iterations * cycle_length
    
    seen_grids[grid_tuple] = current_iteration

# Print final score after reaching or exceeding target iterations
print(score(grid))