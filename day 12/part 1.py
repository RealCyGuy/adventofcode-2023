from itertools import product

from utils.api import get_input

inp = get_input(12)
count = 0
for line in inp.splitlines():
    template, nums = line.split()
    nums = [int(x) for x in nums.split(",")]
    temp = []
    for x in template:
        if x == "?":
            temp.append(["#", "."])
        else:
            temp.append(x)
    for p in product(*temp):
        sp = "".join(p).split(".")
        match = True
        sp = list(filter(None, sp))
        for i, num in enumerate(nums):
            try:
                if len(sp[i]) != num:
                    match = False
                    break
            except IndexError:
                match = False
                break
        if match and len(nums) == len(sp):
            count += 1
print(count)
