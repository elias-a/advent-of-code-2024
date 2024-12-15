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
    return [[x_a, x_b], [y_a, y_b]], [x_prize+10000000000000, y_prize+10000000000000]


def _is_int(num):
    return True if int(num) == num else False


def solve(matrix, b):
    det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    inv = [
        [matrix[1][1]/det, -matrix[0][1]/det],
        [-matrix[1][0]/det, matrix[0][0]/det],
    ]
    solution = [
        inv[0][0]*b[0] + inv[0][1]*b[1],
        inv[1][0]*b[0] + inv[1][1]*b[1],
    ]
    # round in case of numerical issues
    solution = [round(solution[0], 3), round(solution[1], 3)]
    return int(objective(*solution)) if all(_is_int(n) for n in solution) else 0


def objective(a, b):
    return 3*a + b


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    machines = f.read().split("\n\n")
    data = [parse_machine(m) for m in machines]
    tokens = sum(solve(*m) for m in data)
    print(tokens)
