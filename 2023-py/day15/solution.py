# Read input data from the file and split it into a list
with open('input.txt') as file:
    input_lines = file.read().strip().split(',')

# Initialize scores for part 1 and part 2
score_part1 = 0
score_part2 = 0

def compute_hash(string):
    """
    Compute a hash value for a given string using a simple algorithm.
    
    Parameters:
    - string: The input string to hash.

    Returns:
    - An integer hash value.
    """
    hash_value = 0
    for char in string:
        hash_value += ord(char)  # Add ASCII value of the character
        hash_value *= 17         # Multiply by a prime number
        hash_value %= 256        # Keep it within byte range (0-255)
    return hash_value

# Initialize lists to store lens information
lenses = [[] for _ in range(256)]
lens_lengths = [{} for _ in range(256)]

# Process each line from the input
for line in input_lines:
    score_part1 += compute_hash(line)  # Update score for part 1
    
    # Extract label from the line
    label = line.split("=")[0].split("-")[0]
    label_hash = compute_hash(label)  # Compute hash for the label
    
    # Handle lens addition and removal based on the input format
    if "-" in line:  # If there's a '-' in the line, remove the label if it exists
        if label in lenses[label_hash]:
            lenses[label_hash].remove(label)
    
    if "=" in line:  # If there's an '=' in the line, add/update the label
        if label not in lenses[label_hash]:
            lenses[label_hash].append(label)
        lens_lengths[label_hash][label] = int(line.split("=")[1])  # Store lens length

# Calculate score for part 2 based on lens information
for box_index, lens_list in enumerate(lenses):
    for lens_index, lens in enumerate(lens_list):
        score_part2 += (box_index + 1) * (lens_index + 1) * lens_lengths[box_index][lens]

# Print the final scores for both parts
print(score_part1)
print(score_part2)