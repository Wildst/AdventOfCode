#! /usr/bin/python
import sys, getopt
import math
from functools import lru_cache

def to_mask(line):
    return int(line.replace("#", "1").replace(".", "0"),2)

def from_mask(line, size):
    return bin(line)[2:].zfill(size).replace("1", "#").replace("0",".")

def present_width(present):
    return math.ceil(max(present) ** .5)

def print_grid(grid, size=None, prefix=""):
    if not size:
        size = present_width(grid)
    for line in grid:
        print(prefix+from_mask(line, size))
    print()

class Present:
    def __init__(self, lines):
        self.id = int(lines[0][:-1])
        self.shape = lines[1:]
        self.rotations = set()

        shape = self.shape
        for _ in range(4):
            # standard
            self.rotations.add(tuple(map(to_mask, shape)))
            # flipped
            self.rotations.add(tuple(map(to_mask, map(lambda s: s[::-1], shape))))
            shape = [*map("".join,map(reversed,zip(*shape)))]

    def size(self):
        return sum(map(lambda x: x.count("#"), self.shape))

    def __repr__(self):
        return "Present %i (%s rotations): \n\t%s\n" % (self.id, len(self.rotations), "\n\t".join(self.shape))

def add_present(grid, present, pos):
    x, y = pos
    result = [l for l in grid]
    for i, row in enumerate(present):
        if result[y+i] & row << x:
            return False
        result[y+i] += row << x
    return tuple(result)

class PresentCollection:
    def __init__(self, presents):
        self.presents = presents

    @lru_cache(4096)
    def can_fit_presents_in_grid(self, grid_width, grid, presents):
        if not grid:
            return False
        if not sum(presents):
            return True
        present_id = 0
        while not presents[present_id]:
            present_id += 1
        other_presents = [*presents]
        other_presents[present_id] -= 1
        other_presents = tuple(other_presents)
        present = self.presents[present_id]
        for rotation in present.rotations:
            width = present_width(rotation)
            for x in range(grid_width - width+1):
                for y in range(len(grid) - len(rotation)+1):
                    new_grid = add_present(grid, rotation, (x,y))
                    if self.can_fit_presents_in_grid(grid_width, new_grid, other_presents):
                        return True

        return False

def solve_star1():
    *presents, regions = map( lambda x: x.splitlines(), "\n".join(read_file()).split("\n\n"))
    presents = PresentCollection(tuple([*map(Present, presents)]))
    counter = 0
    for i, region in enumerate(regions):
        size, present_list = region.split(": ")
        w,h = map(int, size.split("x"))
        presents_to_add = tuple(map(int, present_list.split()))
        print( "%s/%s" % (counter, i))
        if w * h < sum([presents.presents[present].size() * amount for present, amount in enumerate(presents_to_add)]):
            continue
        if presents.can_fit_presents_in_grid(w, tuple(0 for _ in range(h)), presents_to_add):
            counter += 1
    return counter
def solve_star2():
    return read_file()


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
