
def solve():
    with open('src/main/resources/day01.txt', 'r') as f:
        lines = f.readlines()
    
    current_pos = 50
    zero_count = 0
    total_pos = 100
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'R':
            current_pos = (current_pos + distance) % total_pos
        elif direction == 'L':
            current_pos = (current_pos - distance) % total_pos
            # Python's modulo operator handles negative numbers correctly for this case (e.g. -5 % 100 = 95)
            # but to be explicit and match Java logic:
            # if current_pos < 0: current_pos += total_pos
            # In Python -18 % 100 is 82, so it's fine.
        
        if current_pos == 0:
            zero_count += 1
            
    print(f"Part 1 Answer: {zero_count}")

solve()
