from utils.api import get_input

inp = get_input(10)
grid: list[list[str | int]] = []
clean_grid = []
positions = []  # (x, y, previous)
for y, line in enumerate(inp.splitlines()):
    if "S" in line:
        positions.append((line.index("S"), y))
    grid.append(list(line))
    clean_grid.append(["."] * len(line))
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
        grid[position[1]][position[0]] = 0
        clean_grid[position[1]][position[0]] = tile
    positions = next_positions
count = 0
for y, line in enumerate(clean_grid):
    line = "".join(line)
    for x in range(len(line)):
        tile = line[x]
        if tile == "S":
            top = clean_grid[y - 1][x] in "|7F"
            bottom = clean_grid[y + 1][x] in "|LJ"
            left = clean_grid[y][x - 1] in "-LF"
            right = clean_grid[y][x + 1] in "-J7"
            if top and bottom:
                tile = "|"
            elif left and right:
                tile = "-"
            elif top and left:
                tile = "J"
            elif top and right:
                tile = "L"
            elif bottom and left:
                tile = "7"
            elif bottom and right:
                tile = "F"
            line = list(line)
            line[x] = tile
            line = "".join(line)
        if tile != ".":
            continue
        sub = (
            line[:x]
            .replace(".", "")
            .replace("-", "")
            .replace("L7", "|")
            .replace("FJ", "|")
            .replace("LJ", "")
            .replace("F7", "")
        )
        if sub.count("|") % 2 == 1:
            count += 1
print(count)
