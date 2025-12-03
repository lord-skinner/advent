def parse_input(filename):
    with open(filename, 'r') as file:
        instructions = file.readline().strip()
        file.readline()  # Skip empty line
        network = {}
        for line in file:
            node, connections = line.strip().split(' = ')
            left, right = connections[1:-1].split(', ')
            network[node] = (left, right)
    return instructions, network

def count_steps_to_ZZZ(instructions, network):
    current_node = 'AAA'
    steps = 0
    instruction_index = 0
    
    while current_node != 'ZZZ':
        instruction = instructions[instruction_index]
        if instruction == 'L':
            current_node = network[current_node][0]
        else:  # 'R'
            current_node = network[current_node][1]
        
        steps += 1
        instruction_index = (instruction_index + 1) % len(instructions)
    
    return steps

# Read input and solve
instructions, network = parse_input('input.txt')
steps = count_steps_to_ZZZ(instructions, network)
print(f"Number of steps required to reach ZZZ: {steps}")