def extrapolate_previous(sequence):
    if all(x == 0 for x in sequence):
        return 0
    
    differences = [b - a for a, b in zip(sequence, sequence[1:])]
    prev_diff = extrapolate_previous(differences)
    return sequence[0] - prev_diff

def solve_oasis_report_backwards(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            sequence = list(map(int, line.strip().split()))
            prev_value = extrapolate_previous(sequence)
            total += prev_value
    return total

# Solve the puzzle
result = solve_oasis_report_backwards('input.txt')
print(f"The sum of extrapolated previous values is: {result}")