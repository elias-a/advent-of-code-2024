import os
from maps import Map


def count_func(count, i, j_, visited):
    return count + 1


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    map_ = Map()
    map_.parse([r.strip() for r in f])
    count = map_.make_trails(count_func)
    print(count)
