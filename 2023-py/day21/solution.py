# Load the grid and create a dictionary G where keys are complex numbers (coordinates)
# and values are the characters from the input file.
G = {i + j * 1j: c for i, r in enumerate(open('input.txt')) 
     for j, c in enumerate(r) if c in '.S'}

# Initialize sets for positions of 'S' and a list for tracking states
done = []
todo = {p for p, val in G.items() if val == 'S'}

# Define a function to calculate complex numbers modulo 131
def cmod(p):
    return complex(p.real % 131, p.imag % 131)

# Main loop to simulate state changes for 3 * 131 steps
for step in range(3 * 131):
    if step == 64:
        print(len(todo))  # Print the number of 'S' at step 64
    if step % 131 == 65:
        done.append(len(todo))  # Track the number of 'S' at every step % 131 == 65

    # Update the set of positions to explore (todo) based on neighbors
    next_todo = {p + d for p in todo for d in {1, -1, 1j, -1j} if cmod(p + d) in G}
    todo = next_todo

# Function to calculate a specific formula based on step and done list
def calculate(n, a, b, c):
    return a + n * (b - a + (n - 1) * (c - b - b + a) // 2)

# Output the final result using the formula with the last value of 'done'
print(calculate(26501365 // 131, *done))
