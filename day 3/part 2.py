from utils.api import get_input

inp = get_input(3)
grid = inp.splitlines()
total = 0
for i, line in enumerate(grid):
    num = ""
    for char_i, char in enumerate(line):
        if char == "*":
            numbers = []
            for y in range(i - 1, i + 2):
                streak = 0
                for x in range(char_i - 1, char_i + 2):
                    try:
                        c = grid[y][x]
                    except IndexError:
                        continue
                    if c.isnumeric():
                        if streak > 0:
                            continue
                        streak += 1
                        numbers.append((y, x))
                    else:
                        streak = 0
            if len(numbers) == 2:
                values = []
                for y, x in numbers:
                    value = grid[y][x]
                    for x_go in range(1, 3):
                        try:
                            c = grid[y][x + x_go]
                        except IndexError:
                            pass
                        else:
                            if c.isnumeric():
                                value += c
                            else:
                                break
                    for x_go in range(1, 3):
                        try:
                            c = grid[y][x - x_go]
                        except IndexError:
                            pass
                        else:
                            if c.isnumeric():
                                value = c + value
                            else:
                                break
                    values.append(int(value))
                total += values[0] * values[1]
print(total)
