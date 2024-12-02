import numpy as np

def find_mirror_position(array, axis=0, difference=0):
    """
    Find the mirror position in a 2D array along a specified axis.

    Parameters:
    - array: 2D list of integers (0s and 1s).
    - axis: Axis along which to mirror (0 for rows, 1 for columns).
    - difference: Expected difference between mirrored sections.

    Returns:
    - The index of the row or column where the mirroring condition is satisfied.
    """
    # Convert the input list to a NumPy array for easier manipulation
    matrix = np.array(array, dtype=int)
    
    # Transpose the matrix if mirroring along columns
    if axis == 1:
        matrix = matrix.T
    
    # Iterate through each row (or column) to find the mirror position
    for i in range(matrix.shape[0] - 1):
        # Get the upper part of the matrix flipped
        upper_flipped = np.flip(matrix[:i + 1], axis=0)
        # Get the lower part of the matrix
        lower = matrix[i + 1:]
        
        # Determine how many rows to compare
        rows_to_compare = min(upper_flipped.shape[0], lower.shape[0])
        
        # Check if the difference between upper and lower parts matches the expected difference
        if np.count_nonzero(upper_flipped[:rows_to_compare] - lower[:rows_to_compare]) == difference:
            return i + 1  # Return the index where condition is satisfied
    
    return 0  # Return 0 if no mirror position found

# Read input data from file
with open("input.txt", "r") as file:
    data = file.read().split("\n\n")  # Split data into separate puzzles

# Process each puzzle twice: once with diff=0 and once with diff=1
for diff in range(2):
    total_score = 0
    
    for puzzle in data:
        # Create a list to hold the processed lines of the puzzle
        array = []
        
        for line in puzzle.splitlines():
            # Convert each line into a list of integers (0s and 1s)
            converted_line = [*line.strip().replace(".", "0").replace("#", "1")]
            array.append(converted_line)
        
        # Calculate scores based on mirror positions for rows and columns
        total_score += (
            100 * find_mirror_position(array, axis=0, difference=diff) +
            find_mirror_position(array, axis=1, difference=diff)
        )
    
    print(total_score)  # Output the total score for this difference setting