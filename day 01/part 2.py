from utils.api import get_input

input = get_input(1)
# input = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""
sum = 0
ns = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in input.splitlines():
    values = []
    for n in ns:
        i = 0
        while n in line[i:]:
            i = line.index(n, i)
            values.append((i, ns.index(n) + 1))
            i = i + len(n)
    thing = ""
    if values:
        minm = min(values, key=lambda x: x[0])
        maxm = max(values, key=lambda x: x[0])
    else:
        minm = (1000, 0)
        maxm = (-1000, 0)
    for i, char in enumerate(line):
        if char.isnumeric():
            if i > minm[0]:
                thing += str(minm[1])
            else:
                thing += char
            break
    if len(thing) == 0:
        thing += str(minm[1])
    for i, char in enumerate(reversed(line)):
        i = len(line) - i - 1
        if char.isnumeric():
            if i < maxm[0]:
                thing += str(maxm[1])
            else:
                thing += char
            break
    if len(thing) == 1:
        thing += str(maxm[1])
    sum += int(thing)
print(sum)
