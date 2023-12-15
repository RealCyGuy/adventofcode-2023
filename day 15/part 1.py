from utils.api import get_input

inp = get_input(15)
total = 0
for step in inp.split(","):
    h = 0
    for char in step:
        h += ord(char)
        h *= 17
        h %= 256
    total += h
print(total)
