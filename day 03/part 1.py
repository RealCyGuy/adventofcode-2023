from utils.api import get_input

inp = get_input(3)
grid = inp.splitlines()
total = 0
for i, line in enumerate(grid):
    num = ""
    for char_i, char in enumerate(line + "."):
        if char.isnumeric():
            num += char
        elif num:
            is_part_number = False
            for x in range(char_i - len(num) - 1, char_i + 1):
                for y in range(i - 1, i + 2):
                    if y < 0 or x < 0:
                        continue
                    try:
                        c = grid[y][x]
                        if not c.isnumeric() and c != ".":
                            is_part_number = True
                            break
                    except IndexError:
                        pass
            if is_part_number:
                total += int(num)
            num = ""
print(total)
