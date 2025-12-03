def parse_map(map_data):
    return [list(map(int, line.split())) for line in map_data.strip().split('\n')[1:]]

def apply_map(number, map_data):
    for dest_start, src_start, range_len in map_data:
        if src_start <= number < src_start + range_len:
            return dest_start + (number - src_start)
    return number

def process_seed(seed, maps):
    for map_data in maps:
        seed = apply_map(seed, map_data)
    return seed

# Read input
with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n\n')

seeds = list(map(int, data[0].split(':')[1].split()))
maps = [parse_map(section) for section in data[1:]]

# Process seeds and find lowest location
lowest_location = min(process_seed(seed, maps) for seed in seeds)

print(f"The lowest location number is: {lowest_location}")