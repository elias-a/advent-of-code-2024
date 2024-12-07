import os


class Map:
    def __init__(self, map_):
        self.map_ = map_
        self.coords = {}
        self.current = None
        self.visited = set()

    def parse(self):
        for i, row in enumerate(self.map_):
            for j, c in enumerate(row):
                self.coords[i, j] = c
                if c in ["^", "v", ">", "<"]:
                    self.current = (i, j)
                    self._set_direction(c)

    def visit(self):
        while True:
            if not self._nav_path():
                return self.visited

    def _nav_path(self):
        row_or_col, dir = self.direction
        if row_or_col == "col":
            match dir:
                case -1:
                    path = range(self.current[0], -1, -1)
                    n = ">"
                case 1:
                    path = range(self.current[0], len(self.map_))
                    n = "<"
            for row in path:
                if self.coords[row, self.current[1]] == "#":
                    self.current = (row-dir, self.current[1])
                    self._set_direction(n)
                    break
                self.visited.add((row, self.current[1]))
            else:
                return False
            return True
        elif row_or_col == "row":
            match dir:
                case -1:
                    path = range(self.current[1], -1, -1)
                    n = "^"
                case 1:
                    path = range(self.current[1], len(self.map_[0]))
                    n = "v"
            for col in path:
                if self.coords[self.current[0], col] == "#":
                    self.current = (self.current[0], col-dir)
                    self._set_direction(n)
                    break
                self.visited.add((self.current[0], col))
            else:
                return False
            return True

    def _set_direction(self, c):
        match c:
            case "^":
                self.direction = ("col", -1)
            case "v":
                self.direction = ("col", 1)
            case ">":
                self.direction = ("row", 1)
            case "<":
                self.direction = ("row", -1)


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    map_ = Map([r.strip() for r in f])
    map_.parse()
    visited = map_.visit()
    print(len(visited))
