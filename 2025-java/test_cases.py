#!/usr/bin/env python3
"""
Test specific edge cases with the new formula.
"""

def test_case_v2(start_pos, direction, clicks):
    """Test a specific case with both approaches"""
    print(f"\nTest: Start={start_pos}, {direction}{clicks}")
    
    # Iterative
    position = start_pos
    zero_count_iter = 0
    
    for _ in range(clicks):
        if direction == 'L':
            position = (position - 1) % 100
        else:
            position = (position + 1) % 100
        if position == 0:
            zero_count_iter += 1
    
    # Mathematical v2
    position = start_pos
    if direction == 'R':
        zero_count_math = (position + clicks) // 100
    else:  # L
        if clicks <= position:
            zero_count_math = 0
        else:
            remaining = clicks - position
            zero_count_math = 1 + (remaining - 1) // 100
    
    match = '✅' if zero_count_iter == zero_count_math else '❌'
    print(f"  Iterative: {zero_count_iter}, Mathematical: {zero_count_math} {match}")
    
    if zero_count_iter != zero_count_math:
        # Show the actual path for small cases
        if clicks <= 20:
            position = start_pos
            path = [position]
            for _ in range(clicks):
                if direction == 'L':
                    position = (position - 1) % 100
                else:
                    position = (position + 1) % 100
                path.append(position)
            print(f"  Path: {path}")
            print(f"  Zeros at indices: {[i for i, p in enumerate(path) if p == 0]}")
    
    return zero_count_iter == zero_count_math


# Test the problematic cases
print("="*60)
print("Testing edge cases:")
print("="*60)

test_case_v2(71, 'L', 71)   # Should be 1 (lands exactly on 0)
test_case_v2(0, 'L', 14)    # Should be 0 (starts at 0, goes to 86)
test_case_v2(25, 'L', 725)  # Should be 8
test_case_v2(0, 'L', 308)   # Should be 3
test_case_v2(65, 'R', 37)   # Should be 1
test_case_v2(5, 'L', 10)    # Simple case: 5→4→3→2→1→0→99→98→97→96→95
test_case_v2(5, 'L', 5)     # Exactly lands on 0
test_case_v2(5, 'L', 105)   # Should hit 0 twice: at click 5 and click 105
