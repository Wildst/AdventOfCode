#! /usr/bin/python3.8
import sys, getopt

class Vent:
    def __init__(self, line) -> None:
        self.start, self.end = sorted(map(lambda a: tuple(map(int, a.split(','))),line.split(' -> ')))

    def __repr__(self) -> str:
        return ','.join(map(str, self.start)) + ' -> ' + ','.join(map(str, self.end))

    def is_h_or_v(self):
        return self.is_horizontal() or self.is_vertical()

    def is_horizontal(self):
        return self.start[1] == self.end[1]

    def is_vertical(self):
        return self.start[0] == self.end[0]

    def get_covered_points(self):
        if self.is_horizontal():
            return [(x,self.start[1]) for x in range(self.start[0], self.end[0]+1)]
        elif self.is_vertical():
            return [(self.start[0], y) for y in range(self.start[1], self.end[1]+1)]
        else:
            y_diff = 1 if self.start[1] < self.end[1] else -1
            return [(x, self.start[1] + i*y_diff) for i, x in enumerate(range(self.start[0], self.end[0]+1))]

    def max_x(self):
        return max(self.start[0], self.end[0])

    def max_y(self):
        return max(self.start[1], self.end[1])

def solve_star1():
    vents = [*map(Vent, read_file())]

    grid = [[0 for _ in range(max(map(lambda vent: vent.max_x(), vents))+1)] for _ in range(max(map(lambda vent: vent.max_y(), vents))+1)]

    for vent in vents:
        if vent.is_h_or_v():
            for x,y in vent.get_covered_points():
                grid[y][x] += 1
    return sum(len([i for i in row if i >= 2]) for row in grid)

def solve_star2():
    vents = [*map(Vent, read_file())]

    grid = [[0 for _ in range(max(map(lambda vent: vent.max_x(), vents))+1)] for _ in range(max(map(lambda vent: vent.max_y(), vents))+1)]

    for vent in vents:
        for x,y in vent.get_covered_points():
            grid[y][x] += 1
    return sum(len([i for i in row if i >= 2]) for row in grid)


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][2:-2] + "in"
    file_dir = "input_files"
    star = 1
    try:
        opts, args = getopt.getopt(sys.argv[1:], "12ti:")
    except getopt.GetoptError:
        print("day_<X>.py [12t] [-i <inputfile>]")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-i":
            infile = arg
        elif opt == "-1":
            star = 1
        elif opt == "-2":
            star = 2
        if opt == "-t":
            file_dir = "test_files"

    if star == 1:
        print(solve_star1())
    elif star == 2:
        print(solve_star2())









