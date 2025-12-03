import math
from itertools import cycle

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

def steps_to_z(start, instructions, network):
    current = start
    for step, instruction in enumerate(cycle(instructions), 1):
        current = network[current][0 if instruction == 'L' else 1]
        if current.endswith('Z'):
            return step

def lcm(numbers):
    return math.lcm(*numbers)

def solve(instructions, network):
    start_nodes = [node for node in network if node.endswith('A')]
    cycles = [steps_to_z(node, instructions, network) for node in start_nodes]
    return lcm(cycles)

# Read input and solve
instructions, network = parse_input('input.txt')
result = solve(instructions, network)
print(f"Steps required to reach all Z-ending nodes: {result}")