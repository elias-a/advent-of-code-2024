import os
from itertools import pairwise


def is_increasing(level, next_level):
    return level < next_level


def is_decreasing(level, next_level):
    return level > next_level


def is_constrained(level, next_level):
    return abs(level-next_level) >= 1 and abs(level-next_level) <= 3


def is_report_safe(report):
    increasing = all(is_increasing(l, n) for l, n in pairwise(report))
    decreasing = all(is_decreasing(l, n) for l, n in pairwise(report))
    constrained = all(is_constrained(l, n) for l, n in pairwise(report))
    return (increasing or decreasing) and constrained


def get_reports(original):
    reports = [original]
    for i in range(len(original)):
        report_m = original.copy()
        report_m.pop(i)
        reports.append(report_m)
    return reports


def is_safe(original):
    return any(is_report_safe(r) for r in get_reports(original))


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    reports = [r.strip().split(" ") for r in f]
    num_safe = sum(is_safe([int(l) for l in r]) for r in reports)
    print(num_safe)
