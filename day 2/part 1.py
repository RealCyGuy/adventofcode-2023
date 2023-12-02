from utils.api import get_input

inp = get_input(2).splitlines()
bag = {"red": 12, "green": 13, "blue": 14}
total = 0
for line in inp:
    valid = True
    for round in line.split(":")[-1].split(";"):
        for value in round.split(","):
            n, colour = value.strip().split(" ")
            if int(n) > bag[colour]:
                valid = False
                break
    if valid:
        total += int(line.split(" ")[1].strip(":"))
print(total)
