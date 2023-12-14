from utils.api import get_input

inp = get_input(14)
columns = []

for line in inp.splitlines():
    for i, char in enumerate(line):
        if i + 1 > len(columns):
            columns.append(char)
        else:
            columns[i] += char
total = 0
for column in columns:
    space = 0
    for i, char in enumerate(column):
        match char:
            case "O":
                total += len(column) - i + space
            case "#":
                space = 0
            case ".":
                space += 1
print(total)
