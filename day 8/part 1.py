from utils.api import get_input

inp = get_input(8)
lines = inp.splitlines()
instructions = list(lines[0])
paths = {}
for line in lines[2:]:
    split = [x.strip("(),") for x in line.replace("=", "").split()]
    paths[split[0]] = (split[1], split[2])
current = "AAA"
count = 0
directions = "LR"
while current != "ZZZ":
    instruction = instructions.pop(0)
    instructions.append(instruction)
    current = paths[current][directions.index(instruction)]
    count += 1
print(count)
