import os
import re


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    total = 0
    s = f.read().replace("\n", "")
    groups = re.split(r"(do\(\)|don't\(\))", s)
    do = True
    mul_pattern = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    for group in groups:
        if group not in ["do()", "don't()"] and do:
            for mul in mul_pattern.findall(group):
                a, b = mul
                total += int(a) * int(b)
        elif group == "don't()":
            do = False
        elif group == "do()":
            do = True
    print(total)
