from collections import deque

from utils.api import get_input

inp = get_input(20)

modules = {}
for line in inp.splitlines():
    key, value = line.split(" -> ")
    module = {}
    if key == "broadcaster":
        module["type"] = 0
    else:
        if key.startswith("%"):
            module["type"] = 1
            module["on"] = False
        else:
            module["type"] = 2
            module["watching"] = {}
        key = key[1:]
    module["outputs"] = value.split(", ")
    modules[key] = module
for key, value in modules.items():
    for output in value["outputs"]:
        if "watching" in modules.get(output, {}):
            modules[output]["watching"][key] = False
            if "watched_by" not in value:
                value["watched_by"] = []
            value["watched_by"].append(output)
low = 0
high = 0
for x in range(1000):
    pulses = deque([("broadcaster", False)])
    while pulses:
        name, high_pulse = pulses.popleft()
        if high_pulse:
            high += 1
        else:
            low += 1
        if name not in modules:
            continue
        module = modules[name]
        match module["type"]:
            case 1:
                if high_pulse:
                    continue
                module["on"] = not module["on"]
                high_pulse = module["on"]
            case 2:
                high_pulse = not all(module["watching"].values())
        for watched_by in module.get("watched_by", []):
            modules[watched_by]["watching"][name] = high_pulse
        for p in module["outputs"]:
            pulses.append((p, high_pulse))
print(low * high)
