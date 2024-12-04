"""
M.S
.A.
M.S
"""


import os
from dataclasses import dataclass


@dataclass
class Point:
    i: int
    j: int


@dataclass
class Coordinate(Point):
    letter: str


class WordSearch:
    def __init__(self):
        self.a_coords = []
        self.ms_coords = []
        self.num_xmas = 0

    def parse_row(self, row_num, row):
        for j, c in enumerate(row):
            if c == "A":
                self.a_coords.append(Coordinate(row_num, j, c))
            elif c in ["M", "S"]:
                self.ms_coords.append(Coordinate(row_num, j, c))

    def find_xmas(self):
        for a in self.a_coords:
            if self._check(a):
                self.num_xmas += 1

    def _check(self, a):
        try:
            up_left = next(
                (coord for coord in self.ms_coords
                 if coord.i == a.i - 1 and coord.j == a.j - 1),
            )
            down_right = next(
                (coord for coord in self.ms_coords
                 if coord.i == a.i + 1 and coord.j == a.j + 1),
            )
            up_right = next(
                (coord for coord in self.ms_coords
                 if coord.i == a.i - 1 and coord.j == a.j + 1),
            )
            down_left = next(
                (coord for coord in self.ms_coords
                 if coord.i == a.i + 1 and coord.j == a.j - 1),
            )
        except StopIteration:
            return False
        if up_left.letter == down_right.letter:
            return False
        if up_right.letter == down_left.letter:
            return False
        return True


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    word_search = WordSearch()
    [word_search.parse_row(i, r.strip()) for i, r in enumerate(f)]
    word_search.find_xmas()
    print(word_search.num_xmas)
