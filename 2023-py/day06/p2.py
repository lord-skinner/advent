import math

def calculate_ways_to_win(time, distance):
    # Using the quadratic formula to solve: hold_time * (time - hold_time) > distance
    # This is equivalent to: -hold_time^2 + time*hold_time - distance > 0
    a = -1
    b = time
    c = -distance
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return 0
    
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    # We need to find the number of integer solutions between these roots
    min_hold = math.ceil(min(root1, root2))
    max_hold = math.floor(max(root1, root2))
    
    return max_hold - min_hold + 1

# Read input from file
with open('input.txt', 'r') as file:
    lines = file.readlines()
    time = int(''.join(lines[0].split(':')[1].split()))
    distance = int(''.join(lines[1].split(':')[1].split()))

# Calculate ways to win for the single race
ways_to_win = calculate_ways_to_win(time, distance)

print(f"The number of ways to win the race is: {ways_to_win}")