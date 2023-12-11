from utils.api import get_input

inp = get_input(10)
grid: list[list[str | int]] = []
positions = []  # (x, y, previous)
for y, line in enumerate(inp.splitlines()):
    if "S" in line:
        positions.append((line.index("S"), y))
    grid.append(list(line))
value = 0
while positions:
    next_positions = []
    for position in positions:
        if position[0] < 0 or position[1] < 0:
            continue
        try:
            tile = grid[position[1]][position[0]]
        except IndexError:
            continue
        if isinstance(tile, int) or tile == ".":
            continue
        if len(position) == 3:
            x, y = position[2][:2]
            if x < position[0] and tile not in "-J7":
                continue
            if x > position[0] and tile not in "-LF":
                continue
            if y > position[1] and tile not in "|7F":
                continue
            if y < position[1] and tile not in "|LJ":
                continue
        position = position[:2]
        if tile in "|LJS":
            next_positions.append((position[0], position[1] - 1, position))
        if tile in "|7FS":
            next_positions.append((position[0], position[1] + 1, position))
        if tile in "-LFS":
            next_positions.append((position[0] + 1, position[1], position))
        if tile in "-J7S":
            next_positions.append((position[0] - 1, position[1], position))
        grid[position[1]][position[0]] = value
    value += 1
    positions = next_positions
m = 0
for y in grid:
    for x in y:
        if isinstance(x, int) and x > m:
            m = x
print(m)
