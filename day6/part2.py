import os
from copy import deepcopy


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
                    self.start = (i, j, *self.direction)

    def visit(self):
        while True:
            if not self._nav_path(self.coords):
                return self.visited

    def modify_paths(self, base_visited):
        all_modified_coords = []
        mod_ij = set()
        for i, j, roc, dir in base_visited:
            if (i, j, roc, dir) == self.start:
                continue
            modified_coords = deepcopy(self.coords)
            if (i, j) in mod_ij:
                continue
            modified_coords[i, j] = "#"
            mod_ij.add((i, j))
            all_modified_coords.append(modified_coords)
        return all_modified_coords

    def visit_modified(self, all_modified_coords):
        num = 0
        for coords in all_modified_coords:
            self.visited = set()
            i, j, roc, dir = self.start
            self.current = (i, j)
            self.direction = (roc, dir)
            while True:
                naved = self._nav_path_mod(coords)
                if naved == "LOOP":
                    for i, j, _, _ in self.visited:
                        if coords[i, j] != "^":
                            coords[i, j] = "*"
                    num += 1
                    break
                elif not naved:
                    # out of bounds
                    break
        return num

    def _nav_path_mod(self, coords):
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
                if coords[row, self.current[1]] == "#":
                    self.current = (row-dir, self.current[1])
                    self._set_direction(n)
                    break
                v = (row, self.current[1], row_or_col, dir)
                if v in self.visited:
                    # already visited with this dir, loop
                    return "LOOP"
                self.visited.add(v)
            else:
                # out of bounds
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
                if coords[self.current[0], col] == "#":
                    self.current = (self.current[0], col-dir)
                    self._set_direction(n)
                    break
                v = (self.current[0], col, row_or_col, dir)
                if v in self.visited:
                    # already visited in this dir, loop
                    return "LOOP"
                self.visited.add(v)
            else:
                # out of bounds
                return False
            return True

    def _nav_path(self, coords):
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
                if coords[row, self.current[1]] == "#":
                    self.current = (row-dir, self.current[1])
                    self._set_direction(n)
                    break
                self.visited.add((row, self.current[1], row_or_col, dir))
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
                if coords[self.current[0], col] == "#":
                    self.current = (self.current[0], col-dir)
                    self._set_direction(n)
                    break
                self.visited.add((self.current[0], col, row_or_col, dir))
            else:
                # out of bounds
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
    base_visited = map_.visit()
    all_modified_coords = map_.modify_paths(base_visited)
    num = map_.visit_modified(all_modified_coords)
    print(num)
