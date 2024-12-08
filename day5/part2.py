import os
from collections import defaultdict


class FixUpdates:
    def __init__(self, after_before_map, updates):
        self.after_before_map = after_before_map
        self.updates = updates

    def fix(self):
        return sum(self._fix_update(u) for u in updates)

    def _fix_update(self, update):
        check = self._check(update)
        if not check:
            return 0
        fixed = update.copy()
        while check:
            good = []
            bad = []
            for i in range(len(fixed)):
                if self._check_rest(fixed, i):
                    bad.append(fixed[i])
                else:
                    good.append(fixed[i])
            fixed = good + bad
            check = self._check(fixed)
        return self._get_middle(fixed)

    def _check(self, update):
        return any(self._check_rest(update, i) for i in range(len(update)))

    def _check_rest(self, update, i):
        overlap = set(update[i+1:]).intersection(
            self.after_before_map[update[i]]
        )
        return len(overlap) > 0

    def _get_middle(self, update):
        return int(update[(len(update)-1)//2])


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    rules, updates = f.read().split("\n\n")
    rules = [r.strip() for r in rules.split("\n")]
    updates = [r.strip().split(",") for r in updates.split("\n") if len(r) > 0]
    after_before_map = defaultdict(set)
    for rule in rules:
        before, after = rule.split("|")
        after_before_map[after].add(before)
    fix_updates = FixUpdates(after_before_map, updates)
    middle_sum = fix_updates.fix()
    print(middle_sum)
