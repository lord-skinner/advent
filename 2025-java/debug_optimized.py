#!/usr/bin/env python3
"""
Debug the optimized approach to find where it differs from iterative.
"""

def part2_iterative_debug(data: str) -> int:
    """Original iterative approach with debug output"""
    lines = data.strip().split('\n')
    position = 50
    zero_count = 0
    debug_info = []

    for i, line in enumerate(lines[:10]):  # Just first 10 for debugging
        direction = line[0]
        clicks = int(line[1:])
        
        start_pos = position
        local_zeros = 0

        # Move 1 click at a time
        for _ in range(clicks):
            if direction == 'L':
                position = (position - 1) % 100
            else:  # direction R
                position = (position + 1) % 100

            if position == 0:
                local_zeros += 1
                zero_count += 1
        
        debug_info.append(f"Line {i}: {line.strip()} | Start: {start_pos} → End: {position} | Zeros: {local_zeros}")

    for info in debug_info:
        print(info)
    
    return zero_count


def part2_optimized_debug(data: str) -> int:
    """Optimized mathematical approach with debug output"""
    lines = data.strip().split('\n')
    position = 50
    zero_count = 0
    debug_info = []

    for i, line in enumerate(lines[:10]):  # Just first 10 for debugging
        direction = line[0]
        clicks = int(line[1:])
        
        start_pos = position
        local_zeros = 0

        if direction == 'R':
            local_zeros = (position + clicks) // 100
            zero_count += local_zeros
            position = (position + clicks) % 100
        else:  # direction == 'L'
            if clicks > position:
                local_zeros = (clicks - position + 99) // 100
                zero_count += local_zeros
            position = (position - clicks) % 100
            if position < 0:
                position += 100
        
        debug_info.append(f"Line {i}: {line.strip()} | Start: {start_pos} → End: {position} | Zeros: {local_zeros}")

    for info in debug_info:
        print(info)
    
    return zero_count


if __name__ == "__main__":
    with open('src/main/resources/day01.txt', 'r') as f:
        data = f.read()

    print("=== ITERATIVE (First 10 lines) ===")
    part2_iterative_debug(data)
    
    print("\n=== OPTIMIZED (First 10 lines) ===")
    part2_optimized_debug(data)
