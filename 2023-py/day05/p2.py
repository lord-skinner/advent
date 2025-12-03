def parse_map(map_data):
    return [list(map(int, line.split())) for line in map_data.strip().split('\n')[1:]]

def apply_map(start, length, map_data):
    result = []
    end = start + length
    for dest_start, src_start, range_len in map_data:
        src_end = src_start + range_len
        if start < src_end and end > src_start:
            overlap_start = max(start, src_start)
            overlap_end = min(end, src_end)
            result.append((dest_start + (overlap_start - src_start), overlap_end - overlap_start))
            if overlap_start > start:
                result.extend(apply_map(start, overlap_start - start, map_data))
            if end > overlap_end:
                result.extend(apply_map(overlap_end, end - overlap_end, map_data))
            break
    else:
        result.append((start, length))
    return result

def process_seed_range(start, length, maps):
    ranges = [(start, length)]
    for map_data in maps:
        new_ranges = []
        for range_start, range_length in ranges:
            new_ranges.extend(apply_map(range_start, range_length, map_data))
        ranges = new_ranges
    return min(start for start, _ in ranges)

# Read input
with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n\n')

seed_ranges = list(map(int, data[0].split(':')[1].split()))
maps = [parse_map(section) for section in data[1:]]

# Process seed ranges and find lowest location
lowest_location = float('inf')
for i in range(0, len(seed_ranges), 2):
    start, length = seed_ranges[i], seed_ranges[i+1]
    lowest_location = min(lowest_location, process_seed_range(start, length, maps))

print(f"The lowest location number is: {lowest_location}")