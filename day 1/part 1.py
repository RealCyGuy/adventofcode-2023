from utils.api import get_input

input = get_input(1)
sum = 0
for line in input.splitlines():
    thing = ""
    for char in line:
        if char.isnumeric():
            thing += char
            break
    for char in reversed(line):
        if char.isnumeric():
            thing += char
            break
    sum += int(thing)
print(sum)
