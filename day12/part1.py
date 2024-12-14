import os


class Region:
    def __init__(self, map_):
        self.map_ = map_
        self.perimeter = 0
        self.visited = set()

    def navigate(self, i, j, plant):
        self.visited.add((i, j))
        self._check_neighbor(i-1, j, plant)
        self._check_neighbor(i+1, j, plant)
        self._check_neighbor(i, j-1, plant)
        self._check_neighbor(i, j+1, plant)
        return self.visited, self.perimeter

    def _check_neighbor(self, i, j, plant):
        if (
            (i, j) not in self.visited and
            self._in_grid(i, j) and
            self.map_[i][j] == plant
        ):
            self.navigate(i, j, plant)
        elif not self._in_grid(i, j) or self.map_[i][j] != plant:
            self.perimeter += 1

    def _in_grid(self, i, j):
        return i >= 0 and j >= 0 and i < len(self.map_) and j < len(self.map_[0])


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
            visited, perimeter = region.navigate(i, j, self.map_[i][j])
            self.price += len(visited)*perimeter
            self.not_visited = self.not_visited.difference(visited)
        return self.price


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    map_ = Map()
    map_.parse([list(r.strip()) for r in f])
    price = map_.calc_price()
    print(price)
