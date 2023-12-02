from utils.api import get_input

inp = get_input(2).splitlines()
total = 0
for line in inp:
    bag = {"red": 0, "green": 0, "blue": 0}
    for round in line.split(":")[-1].split(";"):
        for value in round.split(","):
            n, colour = value.strip().split(" ")
            n = int(n)
            if n > bag[colour]:
                bag[colour] = n
    total += bag["red"] * bag["green"] * bag["blue"]
print(total)
