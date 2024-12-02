columns = open("day03.txt", "r").read().splitlines()
location = set()

# get the coordinates of the good numbers
for row_val, row in enumerate(columns):
    for column, col_val in enumerate(row):
        if col_val.isdigit() or col_val =='.':
            continue
        for x in [row_val - 1, row_val, row_val + 1]:
            for y in [column -1, column, column +1]:
                if x < 0 or x >= len(columns) or y < 0 or y >= len(columns[x]) or not columns[x][y].isdigit():
                    continue
                while y > 0 and columns[x][y-1].isdigit():
                    y -= 1
                location.add((x, y))

# add up the good numbers
lst = []
for x , y in location:
    start_point = ''
    while y < len(columns[x]) and columns [x][y].isdigit():
        start_point += columns[x][y]
        y += 1
    lst.append(int(start_point))
print(sum(lst))