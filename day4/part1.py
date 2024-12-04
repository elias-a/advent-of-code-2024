import os
from dataclasses import dataclass


@dataclass
class Point:
    i: int
    j: int


@dataclass
class Direction(Point):
    pass


@dataclass
class Coordinate(Point):
    letter: str


class DirectionSearch:
    def __init__(self, coord, direction, mas_coords):
        self.coord = coord
        self.direction = direction
        self.mas_coords = mas_coords

    def is_xmas(self):
        return all(self._is_valid(letter) for letter in ["M", "A", "S"])

    def _is_valid(self, letter):
        for mas_coord in self.mas_coords:
            if (
                self.coord.i + self.direction.i == mas_coord.i and
                self.coord.j + self.direction.j == mas_coord.j and
                letter == mas_coord.letter
            ):
                self.coord = mas_coord
                return True
        return False


class WordSearch:
    def __init__(self):
        self.x_coords = []
        self.mas_coords = []
        self.num_xmas = 0
        self.directions = [
            Direction(-1, -1),
            Direction(-1, 0),
            Direction(-1, 1),
            Direction(0, -1),
            Direction(0, 0),
            Direction(0, 1),
            Direction(1, -1),
            Direction(1, 0),
            Direction(1, 1),
        ]

    def parse_row(self, row_num, row):
        for j, c in enumerate(row):
            if c == "X":
                self.x_coords.append(Coordinate(row_num, j, c))
            elif c in ["M", "A", "S"]:
                self.mas_coords.append(Coordinate(row_num, j, c))

    def find_xmas(self):
        for x in self.x_coords:
            for direction in self.directions:
                search = DirectionSearch(x, direction, self.mas_coords)
                if search.is_xmas():
                    self.num_xmas += 1


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    word_search = WordSearch()
    [word_search.parse_row(i, r.strip()) for i, r in enumerate(f)]
    word_search.find_xmas()
    print(word_search.num_xmas)
