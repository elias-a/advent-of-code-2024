import os
from itertools import combinations
from collections import defaultdict


class Grid:
    def __init__(self):
        self.grid = []
        self.antennas = defaultdict(set)

    def parse(self, rows):
        for i, row in enumerate(rows):
            grid_row = []
            for j, c in enumerate(row):
                grid_row.append(c)
                if c != ".":
                    self.antennas[c].add((i, j))
            self.grid.append(grid_row)

    def find(self):
        antinodes = set()
        for type_, coords in self.antennas.items():
            for pair in combinations(coords, 2):
                antinodes = antinodes.union(self._find_antinodes(pair))
        return len(antinodes)

    def _find_antinodes(self, coords):
        x, y = self._compute_distance(coords)
        (x1, y1), (x2, y2) = coords
        antinodes = set()
        multiplier = 1
        while True:
            possible = (
                (x1+x*multiplier, y1+y*multiplier),
                (x1-x*multiplier, y1-y*multiplier),
                (x2+x*multiplier, y2+y*multiplier),
                (x2-x*multiplier, y2-y*multiplier),
            )
            multiplier += 1
            a = set(filter(self._in_grid, possible))
            if len(a) == 0:
                break
            antinodes = antinodes.union(a)
        return antinodes

    def _compute_distance(self, coords):
        (x1, y1), (x2, y2) = coords
        return x1 - x2, y1 - y2

    def _in_grid(self, antinode):
        x, y = antinode
        return x >= 0 and y >= 0 and x < len(self.grid) and y < len(self.grid[0])


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    grid = Grid()
    grid.parse([r.strip() for r in f])
    num_antinodes = grid.find()
    print(num_antinodes)
