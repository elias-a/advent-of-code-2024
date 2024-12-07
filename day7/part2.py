import os
from operator import mul, add
from itertools import product


def concat(a, b):
    return int(str(a)+str(b))


def process(row):
    test, equation = row.split(":")
    test = int(test)
    numbers = [int(n) for n in equation.strip().split(" ")]
    operators = [mul, add, concat]
    equations = product(operators, repeat=len(numbers)-1)
    for eq in equations:
        acc = numbers[0]
        for op, num in zip(eq, numbers[1:]):
            acc = op(acc, num)
            if acc > test:
                break
        if acc == test:
            return test
    return 0


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    total = sum(process(r.strip()) for r in f)
    print(total)
