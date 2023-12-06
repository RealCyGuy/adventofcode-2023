from utils.api import get_input

inp = get_input(6)
lines = inp.splitlines()
races = list(zip(lines[0].split(), lines[1].split()))[1:]
total = 1
for time, distance in races:
    time = int(time)
    distance = int(distance)
    count = 0
    for n in range(1, time):
        if n * (time - n) > distance:
            count += 1
    total *= count
print(total)
