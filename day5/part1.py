import os
from collections import defaultdict


def check_update(rules, update):
    pages = update.split(",")
    for i, page in enumerate(pages):
        if len(set(pages[:i]).intersection(rules[page])) > 0:
            break
    else:
        return int(pages[(len(pages)-1)//2])
    return 0


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    rules, updates = f.read().split("\n\n")
    rules = [r.strip() for r in rules.split("\n")]
    updates = [r.strip() for r in updates.split("\n") if len(r) > 0]
    after_rules = defaultdict(set)
    for rule in rules:
        before, after = rule.split("|")
        after_rules[before].add(after)
    middle_sum = sum(check_update(after_rules, u) for u in updates)
    print(middle_sum)
