import os
from collections import defaultdict, deque
from itertools import batched, starmap


def mul_ignore(block, index):
    return block*index if block != "." else 0


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    disk_map = f.read().strip()
    expanded = []
    id_lengths = {}
    free_space = defaultdict(deque)
    id_ = 0
    for pair in batched(disk_map, n=2):
        num, *num_blank = pair
        expanded += [id_]*int(num)
        id_lengths[id_] = int(num)
        id_ += 1
        if len(num_blank) == 1:
            for i in range(1, int(num_blank[0])+1):
                free_space[i].append(len(expanded))
            expanded += ["."]*int(num_blank[0])
    max_id = max(int(b) for b in expanded if isinstance(b, int))
    for id_ in range(max_id, -1, -1):
        if len(free_space[id_lengths[id_]]) == 0:
            continue
        free_index = min(free_space[id_lengths[id_]])
        id_index = expanded.index(id_)
        if free_index > id_index:
            continue
        free_space[id_lengths[id_]].remove(free_index)
        expanded[free_index:free_index+id_lengths[id_]] = [id_]*id_lengths[id_]
        expanded[id_index:id_index+id_lengths[id_]] = ["."]*id_lengths[id_]
        # Update `free_space`.
        length = id_lengths[id_]
        while True:
            if free_index in free_space[length+1]:
                free_space[length+1].remove(free_index)
            else:
                break
            length += 1
        for i in range(1, id_lengths[id_]+1):
            if free_index in free_space[i]:
                free_space[i].remove(free_index)
        for i in range(1, length-id_lengths[id_]+1):
            free_space[i].appendleft(free_index+id_lengths[id_])
    checksum = sum(starmap(mul_ignore, zip(expanded, range(len(expanded)))))
    print(checksum)
