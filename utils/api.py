from typing import AnyStr

import requests
from os.path import exists


def get_input(day: int) -> AnyStr:
    path = f"../inputs/day {day}.txt"

    if not exists(path):
        with open("../cookie.txt") as f:
            cookies = {"session": f.read().strip()}
        response = requests.get(
            f"https://adventofcode.com/2023/day/{day}/input", cookies=cookies
        )
        if not response.ok:
            raise RuntimeError("not ok")
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()
