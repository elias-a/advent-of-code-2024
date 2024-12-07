from itertools import product, accumulate
from collections import deque


def acc_func(total, x):
    op, num = x
    return op(total, num)


def calc(numbers, eq, test):
    acc = accumulate(zip(eq, numbers[1:]), acc_func, initial=numbers[0])
    if deque(acc, maxlen=1).pop() == test:
        return test
    return 0


def process(row, operators):
    test, equation = row.split(":")
    test = int(test)
    numbers = [int(n) for n in equation.strip().split(" ")]
    equations = product(operators, repeat=len(numbers)-1)
    results = (calc(numbers, eq, test) for eq in equations)
    return next(filter(lambda t: t != 0, results), 0)
