import os
from collections import defaultdict


class Region:
    def __init__(self, map_):
        self.map_ = map_
        self.visited = set()
        self.row_edges = defaultdict(set)
        self.col_edges = defaultdict(set)

    def navigate(self, i, j, plant, dir):
        self.visited.add((i, j))
        self._check_neighbor(i-1, j, plant, (-1, 0))
        self._check_neighbor(i+1, j, plant, (1, 0))
        self._check_neighbor(i, j-1, plant, (0, -1))
        self._check_neighbor(i, j+1, plant, (0, 1))
        return self.visited

    def _check_neighbor(self, i, j, plant, dir):
        if (
            (i, j) not in self.visited and
            self._in_grid(i, j) and
            self.map_[i][j] == plant
        ):
            self.navigate(i, j, plant, dir)
        elif not self._in_grid(i, j) or self.map_[i][j] != plant:
            dir_i, dir_j = dir
            if dir_i > 0:
                self.row_edges[i-1, "bottom"].add(j)
            elif dir_i < 0:
                self.row_edges[i+1, "top"].add(j)
            elif dir_j > 0:
                self.col_edges[j-1, "right"].add(i)
            elif dir_j < 0:
                self.col_edges[j+1, "left"].add(i)

    def _in_grid(self, i, j):
        return i >= 0 and j >= 0 and i < len(self.map_) and j < len(self.map_[0])

    def count_edges(self):
        groups = []
        for (row, loc), cols in self.row_edges.items():
            cols = sorted(cols)
            group = []
            for j, col in enumerate(cols):
                if j == 0 or col-1 == cols[j-1]:
                    group.append(col)
                else:
                    groups.append(group)
                    group = [col]
            if len(group) > 0:
                groups.append(group)
        for (col, loc), rows in self.col_edges.items():
            rows = sorted(rows)
            group = []
            for i, row in enumerate(rows):
                if i == 0 or row-1 == rows[i-1]:
                    group.append(row)
                else:
                    groups.append(group)
                    group = [row]
            if len(group) > 0:
                groups.append(group)
        return len(groups)


class Map:
    def __init__(self):
        self.map_ = []
        self.not_visited = set()
        self.price = 0

    def parse(self, rows):
        map_ = []
        not_visited = set()
        for i, row in enumerate(rows):
            row_map = []
            for j, plot in enumerate(row):
                row_map.append(plot)
                not_visited.add((i, j))
            map_.append(row_map)
        self.map_ = map_
        self.not_visited = not_visited

    def calc_price(self):
        while len(self.not_visited) > 0:
            region = Region(self.map_)
            i, j = next(iter(self.not_visited))
            visited = region.navigate(i, j, self.map_[i][j], None)
            num_edges = region.count_edges()
            self.price += len(visited)*num_edges
            self.not_visited = self.not_visited.difference(visited)
        return self.price


def run(test_file):
    with open(os.path.join(os.path.dirname(__file__), test_file), "rt") as f:
        map_ = Map()
        map_.parse([list(r.strip()) for r in f])
        price = map_.calc_price()
        return price


test_files = [
    ("ex.txt", 1206),
    ("ex2.txt", 368),
    ("ex3.txt", 236),
    ("ex4.txt", 436),
]
for test_file, answer in test_files:
    assert run(test_file) == answer
price = run("input.txt")
print(price)
