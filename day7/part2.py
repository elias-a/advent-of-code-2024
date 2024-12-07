import os
from operator import mul, add
from funcs import process


def concat(a, b):
    return int(str(a)+str(b))


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    total = sum(process(r.strip(), [mul, add, concat]) for r in f)
    print(total)
