import os
import re


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    matches = re.findall(r"mul\(([0-9]+),([0-9]+)\)", f.read())
    total = sum(int(a)*int(b) for a, b in matches)
    print(total)
