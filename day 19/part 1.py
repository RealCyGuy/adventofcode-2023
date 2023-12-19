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
for line in two.splitlines():
    values = {}
    for value in line[1:-1].split(","):
        k, v = value.split("=")
        values[k] = int(v)
    next_rule = "in"
    while next_rule not in ("R", "A"):
        steps = rules[next_rule]
        for step in steps:
            if isinstance(step, tuple):
                var = values[step[0]]
                if step[1] == "<":
                    accept = var < step[2]
                else:
                    accept = var > step[2]
                if accept:
                    next_rule = step[3]
                    break
            else:
                next_rule = step
    if next_rule == "A":
        total += sum(values.values())
print(total)
