import os


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    stones = next(r.strip().split(" ") for r in f)
    num_blinks = 25
    for blink in range(num_blinks):
        stones_copy = stones.copy()
        stones = []
        for stone in stones_copy:
            if stone == "0":
                stones.append("1")
            elif len(stone) % 2 == 0:
                stones += [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
            else:
                stones.append(str(int(stone)*2024))
    print(len(stones))
