from utils.api import get_input

inp = get_input(4)
total = 0
next_cards = []
for card in inp.splitlines():
    numbers = card.split(": ")[-1].split(" | ")
    winning = [int(n) for n in numbers[0].split()]
    have = [int(n) for n in numbers[1].split()]
    count = 0
    for n in have:
        if n in winning:
            count += 1
    cards = 1
    if next_cards:
        cards += next_cards.pop(0)
    total += cards
    for x in range(count):
        try:
            next_cards[x] += cards
        except IndexError:
            next_cards.append(cards)
print(total)
