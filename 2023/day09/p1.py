def extrapolate_next(sequence):
    if all(x == 0 for x in sequence):
        return 0
    
    differences = [b - a for a, b in zip(sequence, sequence[1:])]
    next_diff = extrapolate_next(differences)
    return sequence[-1] + next_diff

def solve_oasis_report(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            sequence = list(map(int, line.strip().split()))
            next_value = extrapolate_next(sequence)
            total += next_value
    return total

# Solve the puzzle
result = solve_oasis_report('input.txt')
print(f"The sum of extrapolated values is: {result}")