import os


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    data = (row.strip().split() for row in f)
    zipped = zip(*(sorted(col) for col in zip(*data)))
    distance = sum(abs(int(num1)-int(num2)) for num1, num2 in zipped)
    print(distance)
