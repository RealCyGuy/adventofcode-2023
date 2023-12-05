from utils.api import get_input

inp = get_input(5)
lines = inp.splitlines()
seeds = lines.pop(0).split(": ")[-1].split(" ")

groups = []
group = []
lines.pop(0)
for line in lines + [""]:
    if len(line) == 0:
        groups.append(group)
        group = []
    elif not line.endswith(":"):
        group.append([int(n) for n in line.split(" ")])

location_numbers = []
for seed in seeds:
    value = int(seed)
    for group in groups:
        for destination, source, length in group:
            if source <= value <= source + length:
                value += destination - source
                break
    location_numbers.append(value)
print(min(location_numbers))
