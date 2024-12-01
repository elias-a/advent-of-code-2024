import os
from collections import Counter


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    col1, col2 = zip(*(row.strip().split() for row in f))
    counter = Counter(col2)
    score = sum(int(v)*int(counter[v]) for v in col1)
    print(score)
