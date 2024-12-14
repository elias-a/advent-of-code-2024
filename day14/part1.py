import os
from operator import mul
from functools import reduce
from dataclasses import dataclass, astuple


@dataclass
class Point:
    x: int
    y: int

    def __iter__(self):
        return iter(astuple(self))


class Robot:
    def __init__(self, pos, vel):
        self.pos = Point(*pos)
        self.vel = Point(*vel)


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def parse(self, rows):
        return [self._parse_robot(r) for r in rows]

    def _parse_robot(self, row):
        pos, vel = row.strip().split(" ")
        pos_coords = self._parse_state(pos)
        vel_coords = self._parse_state(vel)
        return Robot(pos_coords, vel_coords)

    def _parse_state(self, state):
        _, coords = state.split("=")
        return self._parse_coords(coords)

    def _parse_coords(self, coords):
        return [int(c) for c in coords.strip().split(",")]


class Simulation:
    def __init__(self, robots, width, height):
        self.robots = robots
        self.width = width
        self.height = height

    def simulate(self):
        [self._advance() for _ in range(100)]

    def _advance(self):
        [self._move_robot(r) for r in self.robots]

    def _move_robot(self, robot):
        robot.pos.x = (robot.pos.x + robot.vel.x) % self.width
        robot.pos.y = (robot.pos.y + robot.vel.y) % self.height

    def count(self):
        y_middle = self.height // 2
        x_middle = self.width // 2
        quadrants = [
            # upper left
            (0, x_middle-1, 0, y_middle-1),
            # upper right
            (x_middle+1, self.width-1, 0, y_middle-1),
            # lower left
            (0, x_middle-1, y_middle+1, self.height-1),
            # lower right
            (x_middle+1, self.width-1, y_middle+1, self.height-1),
        ]
        return reduce(mul, (self._count_quadrant(*lims) for lims in quadrants))

    def _count_quadrant(self, x_left, x_right, y_top, y_bottom):
        count = 0
        for robot in self.robots:
            x, y = robot.pos
            if x >= x_left and x <= x_right and y >= y_top and y <= y_bottom:
                count += 1
        return count


with open(os.path.join(os.path.dirname(__file__), "input.txt"), "rt") as f:
    map_ = Map(width=101, height=103)
    robots = map_.parse([r.strip() for r in f])
    simulation = Simulation(robots, map_.width, map_.height)
    simulation.simulate()
    safety = simulation.count()
    print(safety)
