import itertools

from utils.api import get_input

inp = get_input(5)
lines = inp.splitlines()
seeds_ranges = []
current_range = []
for n in lines.pop(0).split(": ")[-1].split(" "):
    current_range.append(int(n))
    if len(current_range) == 2:
        seeds_ranges.append((current_range[0], current_range[1]))
        current_range = []

groups = []
group = []
lines.pop(0)
for line in lines + [""]:
    if len(line) == 0:
        groups.append(group)
        group = []
    elif not line.endswith(":"):
        group.append([int(n) for n in line.split(" ")])

ranges = seeds_ranges
for group in groups:
    print(ranges)
    next_ranges = []
    for range_start, range_length in ranges:
        used_ranges = []
        for destination, source, length in group:
            start = max(range_start, source)
            end = min(range_start + range_length - 1, source + length - 1)
            if start > end:
                continue
            used_ranges.append((start, end - start + 1))
            next_ranges.append((start + destination - source, end - start + 1))
        same_ranges = [(range_start, range_length)]
        for used_range_start, used_range_length in used_ranges:
            next_same_ranges = []
            for same_range_start, same_range_length in same_ranges:
                same_range_end = same_range_start + same_range_length - 1
                used_range_end = used_range_start + used_range_length - 1
                start = max(used_range_start, same_range_start)
                end = min(used_range_end, same_range_end)
                if start > end:
                    next_same_ranges.append((same_range_start, same_range_length))
                    continue
                if start != same_range_start:
                    next_same_ranges.append(
                        (same_range_start, start - same_range_start + 1)
                    )
                if same_range_end != end:
                    next_same_ranges.append((same_range_end, end - same_range_end + 1))
            same_ranges = next_same_ranges
        for same_range in same_ranges:
            next_ranges.append(same_range)
    ranges = next_ranges
print(min(ranges, key=lambda x: x[0])[0])
