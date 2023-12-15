from utils.api import get_input

inp = get_input(15)
boxes = [[] for x in range(256)]
for step in inp.split(","):
    h = 0
    try:
        pos = step.index("=")
    except ValueError:
        pos = step.index("-")
    label = step[:pos]
    for char in label:
        h += ord(char)
        h *= 17
        h %= 256
    match step[pos]:
        case "=":
            same = False
            for i in range(len(boxes[h])):
                if boxes[h][i][0] == label:
                    same = True
                    boxes[h][i][1] = int(step[pos + 1])
            if not same:
                boxes[h].append([label, int(step[pos + 1])])
        case "-":
            for i in range(len(boxes[h])):
                if boxes[h][i][0] == label:
                    boxes[h].pop(i)
                    break
total = 0
for i, box in enumerate(boxes):
    for i2, slot in enumerate(box):
        total += (i + 1) * slot[1] * (i2 + 1)
print(total)
