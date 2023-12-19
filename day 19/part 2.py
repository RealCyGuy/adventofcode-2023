from copy import deepcopy

from utils.api import get_input

inp = get_input(19)
one, two = inp.split("\n\n")
rules = {}
for line in one.splitlines():
    name, steps = line.split("{")
    formatted = []
    for step in steps.strip("}").split(","):
        if ":" in step:
            i = step.index(":")
            step = (step[0], step[1], int(step[2:i]), step[i + 1 :])
        formatted.append(step)
    rules[name] = tuple(formatted)
total = 0
ranges = [["in", [1, 4001], [1, 4001], [1, 4001], [1, 4001]]]
xmas = "xmas"
while ranges:
    current = ranges.pop(0)
    if current[0] in ("R", "A"):
        if current[0] == "A":
            t = 1
            for x, y in current[1:]:
                t *= y - x
            total += t
        continue
    for step in rules[current[0]]:
        if isinstance(step, tuple):
            var = xmas.index(step[0]) + 1
            value = step[2]
            new = deepcopy(current)
            new[0] = step[3]
            if step[1] == "<":
                if current[var][0] >= value:
                    continue
                current[var][0] = value
                new[var][1] = value
            else:
                if current[var][1] < value:
                    continue
                current[var][1] = value + 1
                new[var][0] = value + 1
            ranges.append(new)
        else:
            current[0] = step
            ranges.append(current)
print(total)
