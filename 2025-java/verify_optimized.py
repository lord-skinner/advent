#!/usr/bin/env python3
"""
FINAL corrected optimized approach.
"""

def part2_optimized_final(data: str) -> int:
    """FINAL corrected optimized mathematical approach - O(n) complexity"""
    lines = data.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])

        if direction == 'R':
            # For right rotation: count how many times we land on 0
            # We land on 0 when (position + k) ≡ 0 (mod 100) for k in [1, clicks]
            # This happens floor((position + clicks) / 100) times
            zero_count += (position + clicks) // 100
            position = (position + clicks) % 100
        else:  # direction == 'L'
            # For left rotation from position p, going k clicks:
            # We hit 0 after exactly p clicks (if k >= p)
            # Then we hit 0 again every 100 clicks after that
            
            # Special case: if we start at 0, we don't count it
            # We only count when we REACH 0, not when we START at 0
            
            if position == 0:
                # Starting at 0, going left
                # We hit 0 again after 100, 200, 300, ... clicks
                if clicks >= 100:
                    zero_count += clicks // 100
            elif clicks >= position:
                # We will hit 0
                # First hit after 'position' clicks
                # Then every 100 clicks: at position+100, position+200, etc.
                # Number of hits = 1 + floor((clicks - position) / 100)
                zero_count += 1 + (clicks - position) // 100
            # else: clicks < position, we never hit 0
            
            position = (position - clicks) % 100
            if position < 0:
                position += 100

    return zero_count


def part2_iterative(data: str) -> int:
    """Original iterative approach - O(n*m) complexity"""
    lines = data.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])

        for _ in range(clicks):
            if direction == 'L':
                position = (position - 1) % 100
            else:
                position = (position + 1) % 100

            if position == 0:
                zero_count += 1
    return zero_count


if __name__ == "__main__":
    with open('src/main/resources/day01.txt', 'r') as f:
        data = f.read()

    iterative_result = part2_iterative(data)
    optimized_result = part2_optimized_final(data)

    print(f"Iterative approach (O(n*m)): {iterative_result}")
    print(f"Optimized approach (O(n)):   {optimized_result}")
    
    if iterative_result == optimized_result:
        print("\n✅ Both approaches produce the same result!")
    else:
        print(f"\n❌ Results differ! Iterative: {iterative_result}, Optimized: {optimized_result}")
