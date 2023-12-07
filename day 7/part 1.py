from collections import Counter

from utils.api import get_input

inp = get_input(7)
hands = []
order = "AKQJT98765432"
order = list(reversed(order))
for line in inp.splitlines():
    hand, score = line.split()
    cards = Counter()
    for char in hand:
        cards[char] += 1
    cards = cards.most_common()
    hand_rank = 0
    if cards[0][1] == 5:
        hand_rank = 6
    elif cards[0][1] == 4:
        hand_rank = 5
    elif cards[0][1] == 3 and cards[1][1] == 2:
        hand_rank = 4
    elif cards[0][1] == 3:
        hand_rank = 3
    elif cards[0][1] == 2 and cards[1][1] == 2:
        hand_rank = 2
    elif cards[0][1] == 2:
        hand_rank = 1
    second_rank = 0
    for i, letter in enumerate(hand):
        second_rank += 100 ** (5 - i) * order.index(letter)
    hands.append((int(score), hand_rank, second_rank, hand))
hands.sort(key=lambda x: x[2])
hands.sort(key=lambda x: x[1])
total = 0
for i, hand in enumerate(hands):
    total += (i + 1) * hand[0]
print(total)
