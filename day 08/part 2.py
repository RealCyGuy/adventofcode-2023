from math import lcm

from utils.api import get_input

inp = get_input(8)
lines = inp.splitlines()
instructions = list(lines[0])
paths = {}
for line in lines[2:]:
    split = [x.strip("(),") for x in line.replace("=", "").split()]
    paths[split[0]] = (split[1], split[2])
current_nodes = []
for start in paths.keys():
    if start.endswith("A"):
        current_nodes.append(start)
count = 0
directions = "LR"
node_numbers = [0 for x in current_nodes]


def check_numbers(numbers):
    for n in numbers:
        if n == 0:
            return False
    return True


while not check_numbers(node_numbers):
    instruction = instructions.pop(0)
    instructions.append(instruction)
    new_nodes = []
    for i, node in enumerate(current_nodes):
        new_nodes.append(paths[node][directions.index(instruction)])
        if node.endswith("Z") and node_numbers[i] == 0:
            node_numbers[i] = count
    count += 1
    current_nodes = new_nodes
print(lcm(*node_numbers))
