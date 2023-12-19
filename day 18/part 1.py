from utils.api import get_input

inp = get_input(18)
grid = [[True]]
pos = [0, 0]
start = [1, 1]
for line in inp.splitlines():
    direction, amount, _ = line.split()
    for x in range(int(amount)):
        match direction:
            case "U":
                pos[1] -= 1
            case "R":
                pos[0] += 1
            case "D":
                pos[1] += 1
            case "L":
                pos[0] -= 1
        if pos[1] < 0:
            start[1] += 1
            grid.insert(0, [False] * (pos[0] + 1))
            pos[1] += 1
        if pos[0] < 0:
            start[0] += 1
            for y in grid:
                y.insert(0, False)
            pos[0] += 1
        if len(grid) < pos[1] + 1:
            grid.append([False] * (pos[0] + 1))
        while len(grid[pos[1]]) < pos[0] + 1:
            grid[pos[1]].append(False)
        grid[pos[1]][pos[0]] = True

points = set()
points.add(tuple(start))
while points:
    x, y = points.pop()
    print(x, y)
    try:
        tile = grid[y][x]
    except IndexError:
        continue
    if tile:
        continue
    grid[y][x] = True
    points.add((x + 1, y))
    points.add((x - 1, y))
    points.add((x, y + 1))
    points.add((x, y - 1))


count = 0
for y, line in enumerate(grid):
    for x in range(len(line)):
        if line[x] is True:
            count += 1
print(count)
