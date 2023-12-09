from utils.api import get_input

inp = get_input(9)
total = 0

for line in inp.splitlines():
    sequences = [[int(x) for x in line.split()]]
    while any(sequences[-1]):
        current_s = sequences[-1]
        next_s = []
        for x in range(len(current_s) - 1):
            next_s.append(current_s[x + 1] - current_s[x])
        sequences.append(next_s)
    for s in sequences:
        total += s[-1]
print(total)
