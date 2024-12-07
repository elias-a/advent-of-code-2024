import os
from operator import mul, add
from funcs import process


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    total = sum(process(r.strip(), [mul, add]) for r in f)
    print(total)
