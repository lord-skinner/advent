ans1 = 0
for game_num, game_info in enumerate(open("day02.txt", "r")):
    games = game_info.split(": ")[1].split("; ")
    for game in games:
        map = {"red": 0, "green": 0, "blue": 0}
        for cubes in game.split(", "):
            a, b = cubes.split()
            map[b] = int(a)
        if map["red"] > 12 or map["green"] > 13 or map["blue"] > 14:
            break
    else:
        ans1 += game_num +1
print(ans1)