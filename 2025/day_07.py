#! /usr/bin/python
import sys, getopt
from functools import lru_cache

def solve_star1():
    grid = read_file()
    beams = set()
    beams.add(grid[0].index("S"))
    counter = 0
    for line in grid[1:]:
        new_beams = set()
        for beam in beams:
            if line[beam] == "^":
                new_beams.add(beam -1)
                new_beams.add(beam +1)
                counter += 1
            elif line[beam] == ".":
                new_beams.add(beam)
        beams = new_beams
    return counter

class Grid:
    def __init__(self, lines):
        self.lines = lines

    @lru_cache
    def count_timelines(self, beam, line):
        if line >= len(self.lines):
            return 1
        if self.lines[line][beam] == "^":
            return self.count_timelines(beam-1, line+1) \
                 + self.count_timelines(beam+1, line+1)
        else:
            return self.count_timelines(beam, line + 1)

def solve_star2():
    grid = Grid(read_file())
    return grid.count_timelines(grid.lines[0].index("S"), 0)


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][0:-2] + "in"
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
