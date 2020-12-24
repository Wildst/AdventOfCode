#! /usr/bin/python
import sys, getopt


"""
        # #
       # # #
        # #
"""

DIRECTIONS = {
    "e": (1, 0),
    "se": (1, 1),
    "sw": (0, 1),
    "w": (-1, 0),
    "nw": (-1, -1),
    "ne": (0, -1)
}

def direction_add(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])

def solve_star1():
    tiles = {}
    for line in read_file():
        pos = 0, 0
        direction = ""
        for char in line:
            direction += char
            if direction in DIRECTIONS:
                pos = direction_add(pos, DIRECTIONS[direction])
                direction = ""
        if pos in tiles:
            tiles[pos] ^= True
        else:
            tiles[pos] = True
    print(len([t for t in tiles.values() if t]))


class Tile():
    def __init__(self, pos, black=False):
        self.pos = pos
        self.black = black
        self.black_neighbours = 0

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Tile at " + str(self.pos) + " is " + ("black" if self.black else "white")

    def flip(self):
        self.black ^= True

    def check_color(self):
        if self.black:
            if self.black_neighbours == 0 or self.black_neighbours > 2:
                self.black = False
        else:
            if self.black_neighbours == 2:
                self.black = True

    def recount(self):
        self.black_neighbours = 0

    def get_neighbours(self):
        return [direction_add(self.pos, direction) for direction in DIRECTIONS.values()]



"""
Round 0
             . . . # .
              . . . . .
             # # . . . . .
            # . X . # . . .
             # . . .
          . # . . #
             # .
Round 1
             . . . . .
            . # . . . .
           # # # # . . . .
          . # . X # . . . .
           . # # # #
          . # . . . .
           # # .

"""
def solve_star2():
    tiles = {}
    for line in read_file():
        pos = 0, 0
        direction = ""
        for char in line:
            direction += char
            if direction in DIRECTIONS:
                pos = direction_add(pos, DIRECTIONS[direction])
                direction = ""
        if pos in tiles:
            tiles[pos].flip()
        else:
            tiles[pos] = Tile(pos, True)

    for i in range(100):
        to_add = set()
        for tile in tiles.values():
            tile.recount()
            if tile.black:
                for neighbour in tile.get_neighbours():
                    if not neighbour in tiles:
                        to_add.add(neighbour)
        for pos in to_add:
            tiles[pos] = Tile(pos, False)

        for tile in tiles.values():
            if tile.black:
                for neighbour in tile.get_neighbours():
                    tiles[neighbour].black_neighbours += 1

        for tile in tiles.values():
            tile.check_color()

    print(len([t for t in tiles.values() if t.black]))


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
        solve_star1()
    elif star == 2:
        solve_star2()









