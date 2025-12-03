ans2 = 0
for game_num, game_info in enumerate(open("day02.txt", "r")):
    games = game_info.split(": ")[1].split("; ")
    total_map = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        map = {"red": 0, "green": 0, "blue": 0}
        for cubes in game.split(", "):
            a, b = cubes.split()
            map[b] = int(a)
        for total_map_key in total_map:
            total_map[total_map_key] = max(total_map[total_map_key], map[total_map_key])
    ans2 += total_map["red"] * total_map["green"] * total_map["blue"]
print(ans2)