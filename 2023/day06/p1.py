def calculate_distance(hold_time, total_time):
    return hold_time * (total_time - hold_time)

def count_ways_to_win(time, record_distance):
    ways_to_win = 0
    for hold_time in range(time + 1):
        distance = calculate_distance(hold_time, time)
        if distance > record_distance:
            ways_to_win += 1
    return ways_to_win

# Read input from file
with open('input.txt', 'r') as file:
    lines = file.readlines()
    times = list(map(int, lines[0].split(':')[1].split()))
    distances = list(map(int, lines[1].split(':')[1].split()))

# Calculate ways to win for each race
ways_to_win_per_race = [count_ways_to_win(t, d) for t, d in zip(times, distances)]

# Calculate the final result
result = 1
for ways in ways_to_win_per_race:
    result *= ways

print(f"The product of the number of ways to win each race is: {result}")