# brute forcing works fine lol

from utils.api import get_input

inp = get_input(6)
lines = inp.splitlines()
count = 0
time = int(lines[0].split(":")[-1].replace(" ", ""))
distance = int(lines[1].split(":")[-1].replace(" ", ""))
for n in range(1, time):
    if n * (time - n) > distance:
        count += 1
print(count)
