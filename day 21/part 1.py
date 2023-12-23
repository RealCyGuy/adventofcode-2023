from utils.api import get_input

inp = get_input(21)
grid = []
positions = set()
for y, line in enumerate(inp.splitlines()):
    l = []
    for x, char in enumerate(line):
        l.append(char == "#")
        if char == "S":
            positions.add((x, y))
    grid.append(l)
for x in range(64):
    new_positions = set()
    for x, y in positions:
        for direction in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if new_x < 0 or new_y < 0:
                continue
            try:
                tile = grid[new_y][new_x]
            except IndexError:
                continue
            if tile:
                continue
            new_positions.add((new_x, new_y))
    positions = new_positions
print(len(positions))
