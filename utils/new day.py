import os

for x in range(1, 33):
    path = f"../day {x}"
    if not os.path.exists(path):
        os.mkdir(path)
        for part in range(1, 3):
            with open(os.path.join(path, f"part {part}.py"), "w") as f:
                f.write(f"from utils.api import get_input\n\ninp = get_input({x})\n")
        print(f"Created day {x}! Good luck.")
        break
