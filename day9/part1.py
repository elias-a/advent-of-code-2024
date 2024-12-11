import os
from operator import mul
from collections import deque
from itertools import batched, starmap


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    disk_map = f.read().strip()
    expanded = deque()
    id_ = 0
    for pair in batched(disk_map, n=2):
        num, *num_blank = pair
        expanded += [id_]*int(num)
        id_ += 1
        if len(num_blank) == 1:
            expanded += ["."]*int(num_blank[0])
    while expanded.count(".") > 0:
        block = expanded.pop()
        if block == ".":
            continue
        expanded[expanded.index(".")] = block
    checksum = sum(starmap(mul, zip(expanded, range(len(expanded)))))
    print(checksum)
