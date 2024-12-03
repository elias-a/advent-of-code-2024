import os
from itertools import pairwise


def is_safe(report):
    pairs = list(pairwise(report))
    increasing = all(l < n for l, n in pairs)
    decreasing = all(l > n for l, n in pairs)
    adjacency = all(abs(l-n) >= 1 and abs(l-n) <= 3 for l, n in pairs)
    return (increasing or decreasing) and adjacency


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    reports = [r.strip().split(" ") for r in f]
    num_safe = sum(is_safe(int(l) for l in r) for r in reports)
    print(num_safe)
