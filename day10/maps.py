

class Trailhead:
    def __init__(self, map_, trailhead, max_i, max_j):
        self.map_ = map_
        self.trailhead = trailhead
        self.max_i = max_i
        self.max_j = max_j
        self.visited = set()
        self.count = 0

    def make_trail(self, count_func):
        self.count_func = count_func
        i, j = self.trailhead
        self._step(i-1, j, 0)
        self._step(i+1, j, 0)
        self._step(i, j-1, 0)
        self._step(i, j+1, 0)
        return self.count

    def _step(self, i, j, score):
        if not self._in_grid(i, j):
            return
        next_score = self.map_[i, j]
        if next_score != score + 1:
            return
        if next_score == 9:
            self.count = self.count_func(self.count, i, j, self.visited)
            self.visited.add((i, j))
            return
        self._step(i-1, j, next_score)
        self._step(i+1, j, next_score)
        self._step(i, j-1, next_score)
        self._step(i, j+1, next_score)

    def _in_grid(self, i, j):
        return i >= 0 and j >= 0 and i <= self.max_i and j <= self.max_j


class Map:
    def __init__(self):
        self.map_ = {}
        self.trailheads = set()
        self.max_i = 0
        self.max_j = 0

    def parse(self, rows):
        for i, row in enumerate(rows):
            for j, c in enumerate(row):
                score = int(c)
                self.map_[i, j] = score
                if score == 0:
                    self.trailheads.add((i, j))
        self.max_i, self.max_j = max(self.map_.keys())

    def make_trails(self, count_func):
        trailheads = [Trailhead(self.map_, h, self.max_i, self.max_j)
                      for h in self.trailheads]
        return sum(h.make_trail(count_func) for h in trailheads)
