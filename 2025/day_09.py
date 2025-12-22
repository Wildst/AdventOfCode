#! /usr/bin/python
import sys, getopt
from functools import lru_cache

class Tile:
    def __init__(self, line):
        self.x, self.y = map(int, line.split(","))

    def __repr__(self):
        return "Tile(%s, %s)" % (self.x, self.y)

class Rectangle:
    def __init__(self, tile1, tile2):
        self.t1 = tile1
        self.t2 = tile2

    def size(self):
        return (abs(self.t1.x - self.t2.x) + 1) * (abs(self.t1.y - self.t2.y) + 1)

def solve_star1():
    tiles = [Tile(line) for line in read_file()]
    rectangles = []
    for i, tile in enumerate(tiles[:-1]):
        for other in tiles[i+1:]:
            rectangles.append(Rectangle(tile, other))

    return max(map(lambda r: r.size(), rectangles))

class Simplification:
    def __init__(self, tiles):
        self.all_x = sorted(set(tile.x for tile in tiles))
        self.all_y = sorted(set(tile.y for tile in tiles))

        # Collect corners
        simple_tiles = [*map(self.simplify_tile, tiles)]
        self.simple_tiles = set(simple_tiles)

        self.max_x = max(x for x,y in self.simple_tiles)
        self.max_y = max(y for x,y in self.simple_tiles)

        # Make edges
        previous = simple_tiles[-1]
        for tile in simple_tiles:
            x1, y1 = tile
            x2, y2 = previous
            if x1 == x2:
                for y in range(min(y1, y2)+1,max(y1, y2)):
                    self.simple_tiles.add((x1, y))
            elif y1 == y2:
                for x in range(min(x1, x2)+1,max(x1, x2)):
                    self.simple_tiles.add((x, y1))
            previous = tile

        # fill center
        for x in range(self.max_x):
            for y in range(self.max_y):
                if self.is_contained(x,y):
                    self.simple_tiles.add((x,y))

    def simplify_tile(self, tile):
        return (self.all_x.index(tile.x), self.all_y.index(tile.y))

    def is_bound(self, pos, direction):
        if pos in self.simple_tiles:
            return True
        x, y = pos
        if not 0 < x < self.max_x:
            return False
        if not 0 < y < self.max_y:
            return False
        dx, dy = direction
        return self.is_bound((x+dx, y+dy), direction)

    def is_contained(self, x, y):
        return  self.is_bound((x,y), ( 0,  1))\
            and self.is_bound((x,y), ( 1,  0))\
            and self.is_bound((x,y), ( 0, -1))\
            and self.is_bound((x,y), (-1,  0))


    def is_valid(self, rectangle):
        x1, y1 = self.simplify_tile(rectangle.t1)
        x2, y2 = self.simplify_tile(rectangle.t2)
        for x in range(min(x1, x2), max(x1,x2)+1):
            for y in range(min(y1, y2), max(y1,y2)+1):
                if (x,y) not in self.simple_tiles:
                    return False
        return True


    def print_grid(self):
        max_x = max(map(lambda t: t[0], self.simple_tiles))
        max_y = max(map(lambda t: t[1], self.simple_tiles))
        grid = []
        for y in range(max_y+2):
            line = []
            for x in range(max_x+3):
                line.append(".")
            grid.append(line)
        for tile in self.simple_tiles:
            x, y = tile
            grid[y][x] = "#"
        for line in grid:
            print("".join(line))


def solve_star2():
    tiles = [Tile(line) for line in read_file()]
    simplification = Simplification(tiles)

    rectangles = []
    for i, tile in enumerate(tiles[:-1]):
        for other in tiles[i+1:]:
            rectangles.append(Rectangle(tile, other))

    good_rectangles = [ r for r  in rectangles if simplification.is_valid(r)]

    return max(map(lambda r: r.size(), good_rectangles))


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
