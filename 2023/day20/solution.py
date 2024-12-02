import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, deque
import heapq
import math

# Read input data
input_data = open('input.txt').read().strip()
lines = input_data.split('\n')
grid = [[c for c in row] for row in lines]
rows = len(grid)
cols = len(grid[0])

# Function to calculate the Least Common Multiple (LCM) of a list of numbers
def calculate_lcm(numbers):
    result = 1
    for number in numbers:
        result = (result * number) // math.gcd(number, result)
    return result

# Initialize mappings and data structures
type_mapping = {}
relationship = {}
for line in lines:
    source, destination = line.split('->')
    source = source.strip()
    destination = destination.strip().split(', ')
    relationship[source] = destination
    type_mapping[source[1:]] = source[0]

# Adjust function to map the type of elements
def adjust_element(element):
    if element in type_mapping:
        return type_mapping[element] + element
    else:
        return element

# Create dictionaries to manage relationships
reverse_relationship = {}
inverse_relationship = defaultdict(list)

for source, destinations in relationship.items():
    relationship[source] = [adjust_element(dest) for dest in destinations]
    for destination in relationship[source]:
        if destination[0] == '&':
            if destination not in reverse_relationship:
                reverse_relationship[destination] = {}
            reverse_relationship[destination][source] = 'lo'
        inverse_relationship[destination].append(source)

# Ensure that 'rx' has exactly one inverse relationship
assert len(inverse_relationship['rx']) == 1
assert inverse_relationship['rx'][0][0] == '&'

# Watch the inverse of the first relationship of 'rx'
watch_list = inverse_relationship[inverse_relationship['rx'][0]]

# Initialize counters and queues for the simulation
lo_count = 0
hi_count = 0
queue = deque()
active_elements = set()
previous_timestamp = {}
count_map = defaultdict(int)
to_lcm_values = []

# Start the simulation loop
for timestamp in range(1, 10**8):
    queue.append(('broadcaster', 'button', 'lo'))

    while queue:
        element, from_element, element_type = queue.popleft()

        # Process 'lo' type elements
        if element_type == 'lo':
            if element in previous_timestamp and count_map[element] == 2 and element in watch_list:
                # Track the cycle period when elements in watch_list get 'lo' inputs
                to_lcm_values.append(timestamp - previous_timestamp[element])
            previous_timestamp[element] = timestamp
            count_map[element] += 1

        # If we have collected enough data, calculate the LCM and exit
        if len(to_lcm_values) == len(watch_list):
            print(calculate_lcm(to_lcm_values))
            sys.exit(0)

        # If 'rx' is processed with 'lo', print the timestamp and exit (unreachable case in practice)
        if element == 'rx' and element_type == 'lo':
            print(timestamp + 1)

        # Increment the 'lo' or 'hi' counter
        if element_type == 'lo':
            lo_count += 1
        else:
            hi_count += 1

        # Continue if there are no relationships for the current element
        if element not in relationship:
            continue

        # Handle special cases for 'broadcaster', '%' and '&' elements
        if element == 'broadcaster':
            for destination in relationship[element]:
                queue.append((destination, element, element_type))
        elif element[0] == '%':
            if element_type == 'hi':
                continue
            else:
                # Toggle the state of '%' elements
                if element not in active_elements:
                    active_elements.add(element)
                    new_type = 'hi'
                else:
                    active_elements.discard(element)
                    new_type = 'lo'
                for destination in relationship[element]:
                    queue.append((destination, element, new_type))
        elif element[0] == '&':
            # Update the state of '&' elements based on their relationships
            reverse_relationship[element][from_element] = element_type
            new_type = 'lo' if all(value == 'hi' for value in reverse_relationship[element].values()) else 'hi'
            for destination in relationship[element]:
                queue.append((destination, element, new_type))
        else:
            assert False, f"Unexpected element type: {element}"

    # Check for the lo*hi result at timestamp 1000
    if timestamp == 1000:
        print(lo_count * hi_count)
