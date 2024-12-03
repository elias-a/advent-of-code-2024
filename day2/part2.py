import os
from itertools import pairwise


def is_increasing(level, next_level):
    return level < next_level


def is_decreasing(level, next_level):
    return level > next_level


def is_constrained(level, next_level):
    return abs(level-next_level) >= 1 and abs(level-next_level) <= 3


def check(report, func):
    for i in range(len(report)):
        report_m = report.copy()
        report_m.pop(i)
        if all(func(l, n) for l, n in pairwise(report_m)):
            return True
    return False


def is_safe(report):
    increasing = check(report, is_increasing)
    decreasing = check(report, is_decreasing)
    constrained = check(report, is_constrained)
    return (increasing or decreasing) and constrained


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    reports = [r.strip().split(" ") for r in f]
    num_safe = sum(is_safe([int(l) for l in r]) for r in reports)
    print(num_safe)
