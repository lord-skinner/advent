from heapq import heappop, heappush

# Read input from the file and create a grid representation with costs
grid = {
    i + j * 1j: int(cost)  # Use complex numbers as keys for grid positions
    for i, row in enumerate(open('input.txt'))
    for j, cost in enumerate(row.strip())
}

def find_min_cost(min_range, max_range, end_position=None, step_count=0):
    """
    Find the minimum cost to reach the end position in the grid.

    Parameters:
    - min_range: Minimum step size.
    - max_range: Maximum step size.
    - end_position: The target position to reach (default is the last position in the grid).
    - step_count: Counter for steps taken (used for tracking).

    Returns:
    - The minimum cost to reach the end position.
    """
    
    if end_position is None:
        end_position = list(grid.keys())[-1]  # Set default end position to the last key in grid

    # Initialize priority queue with starting positions and directions
    todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]  # (cost, step_count, current_position, direction)
    visited = set()  # Set to track visited positions and directions

    while todo:
        current_cost, _, current_position, current_direction = heappop(todo)

        # If we reached the end position, return the current cost
        if current_position == end_position:
            return current_cost
        
        # Skip already visited positions with the same direction
        if (current_position, current_direction) in visited:
            continue
        
        visited.add((current_position, current_direction))  # Mark this position and direction as visited

        # Explore new directions based on current direction
        for new_direction in [1j / current_direction, -1j / current_direction]:
            for step_size in range(min_range, max_range + 1):
                next_position = current_position + new_direction * step_size
                
                if next_position in grid:
                    # Calculate the cost of moving to this new position
                    move_cost = sum(grid[current_position + new_direction * j] for j in range(1, step_size + 1))
                    heappush(todo, (current_cost + move_cost, (step_count := step_count + 1), next_position, new_direction))

# Print results for specified ranges
print(find_min_cost(1, 3), find_min_cost(4, 10))