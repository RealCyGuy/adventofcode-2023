from utils.api import get_input

inp = get_input(4)
total = 0
for card in inp.splitlines():
    numbers = card.split(": ")[-1].split(" | ")
    winning = [int(n) for n in numbers[0].split()]
    have = [int(n) for n in numbers[1].split()]
    count = 0
    for n in have:
        if n in winning:
            count += 1
    if count > 0:
        total += 2 ** (count - 1)
print(total)
