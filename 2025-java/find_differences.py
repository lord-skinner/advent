#!/usr/bin/env python3
"""
Find the first line where iterative and optimized differ.
"""

def part2_iterative_full(data: str):
    """Original iterative approach - returns list of (line_num, zeros_for_this_line)"""
    lines = data.strip().split('\n')
    position = 50
    results = []

    for i, line in enumerate(lines):
        direction = line[0]
        clicks = int(line[1:])
        
        start_pos = position
        local_zeros = 0

        for _ in range(clicks):
            if direction == 'L':
                position = (position - 1) % 100
            else:
                position = (position + 1) % 100

            if position == 0:
                local_zeros += 1
        
        results.append((i, line.strip(), start_pos, position, local_zeros))

    return results


def part2_optimized_full(data: str):
    """Optimized mathematical approach - returns list of (line_num, zeros_for_this_line)"""
    lines = data.strip().split('\n')
    position = 50
    results = []

    for i, line in enumerate(lines):
        direction = line[0]
        clicks = int(line[1:])
        
        start_pos = position
        local_zeros = 0

        if direction == 'R':
            local_zeros = (position + clicks) // 100
            position = (position + clicks) % 100
        else:  # direction == 'L'
            if clicks > position:
                local_zeros = (clicks - position + 99) // 100
            position = (position - clicks) % 100
            if position < 0:
                position += 100
        
        results.append((i, line.strip(), start_pos, position, local_zeros))

    return results


if __name__ == "__main__":
    with open('src/main/resources/day01.txt', 'r') as f:
        data = f.read()

    iterative = part2_iterative_full(data)
    optimized = part2_optimized_full(data)

    print("Finding differences...")
    differences = []
    
    for (i1, line1, start1, end1, zeros1), (i2, line2, start2, end2, zeros2) in zip(iterative, optimized):
        if zeros1 != zeros2:
            differences.append({
                'line_num': i1,
                'instruction': line1,
                'start': start1,
                'end': end1,
                'iterative_zeros': zeros1,
                'optimized_zeros': zeros2
            })
    
    if differences:
        print(f"\nFound {len(differences)} differences:")
        for diff in differences[:20]:  # Show first 20
            print(f"Line {diff['line_num']}: {diff['instruction']} | "
                  f"Start: {diff['start']} → End: {diff['end']} | "
                  f"Iterative: {diff['iterative_zeros']}, Optimized: {diff['optimized_zeros']}")
    else:
        print("No differences found!")
    
    total_iter = sum(r[4] for r in iterative)
    total_opt = sum(r[4] for r in optimized)
    print(f"\nTotal - Iterative: {total_iter}, Optimized: {total_opt}, Difference: {total_opt - total_iter}")
