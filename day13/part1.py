import os


def _parse_row(button, sep="+"):
    _, config = button.split(":")
    x, y = config.split(",")
    _, x_num = x.split(sep)
    _, y_num = y.split(sep)
    return int(x_num), int(y_num)


def parse_machine(machine):
    button_a, button_b, prize = machine.strip().split("\n")
    x_a, y_a = _parse_row(button_a)
    x_b, y_b = _parse_row(button_b)
    x_prize, y_prize = _parse_row(prize, sep="=")
    return x_a, y_a, x_b, y_b, x_prize, y_prize


def solve(x_a, y_a, x_b, y_b, x_prize, y_prize):
    valid = []
    for a in range(100):
        for b in range(100):
            if a*x_a + b*x_b == x_prize and a*y_a + b*y_b == y_prize:
                valid.append((a, b))
    if len(valid) == 0:
        return 0
    return min(objective(*n) for n in valid)


def objective(a, b):
    return 3*a + b


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    machines = f.read().split("\n\n")
    data = [parse_machine(m) for m in machines]
    tokens = sum([solve(*m) for m in data])
    print(tokens)
