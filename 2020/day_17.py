#! /usr/bin/python
import sys, getopt

class Cube():
    def __init__(self, pos, state):
        self.x, self.y, self.z = pos
        self.active = state == "#"
        self.active_neighbour_count = 0

    def get_pos(self):
        return (self.x, self.y, self.z)

    def get_neighbours(self):
        return [ (self.x +i, self.y + j, self.z + k) for k in range(-1, 2) for j in range(-1, 2) for i in range(-1, 2) if not (i==0 and j==0 and k==0) ]

    def __str__(self):
        return str(self.get_pos()) + " " + ("Active" if self.active else "Inactive")

    def __repr__(self):
        return str(self)

    def recount(self):
        self.active_neighbour_count = 0

    def check_activation(self):
        if self.active:
            self.active = self.active_neighbour_count in [2, 3]
        else:
            self.active = self.active_neighbour_count == 3

def solve_star1():
    cubes = {}
    for y, line in enumerate(read_file()):
        for x, c in enumerate(line):
            cubes[(x, y, 0)] = Cube((x, y, 0), c)

    for i in range(6):
        # create neighbours if necesary
        needed_cubes = set()
        for cube in cubes.values():
            if cube.active:
                needed_cubes |= set(cube.get_neighbours())
        for position in needed_cubes:
            if not position in cubes:
                cubes[position] = Cube(position, False)

        # recount all neighbours
        for cube in cubes.values():
            cube.recount()
        for cube in cubes.values():
            if cube.active:
                for position in cube.get_neighbours():
                    cubes[position].active_neighbour_count += 1

        # check activation
        for cube in cubes.values():
            cube.check_activation()

    print(len([cube for cube in cubes.values() if cube.active]))



class HyperCube():
    def __init__(self, pos, state):
        self.x, self.y, self.z, self.w = pos
        self.active = state == "#"
        self.active_neighbour_count = 0

    def get_pos(self):
        return (self.x, self.y, self.z, self.w)

    def get_neighbours(self):
        return [ (self.x +i, self.y + j, self.z + k, self.w + l)
                    for l in range(-1, 2)
                    for k in range(-1, 2)
                    for j in range(-1, 2)
                    for i in range(-1, 2)
                    if not (i==0 and j==0 and k==0 and l == 0) ]

    def __str__(self):
        return str(self.get_pos()) + " " + ("Active" if self.active else "Inactive")

    def __repr__(self):
        return str(self)

    def recount(self):
        self.active_neighbour_count = 0

    def check_activation(self):
        if self.active:
            self.active = self.active_neighbour_count in [2, 3]
        else:
            self.active = self.active_neighbour_count == 3

def solve_star2():
    cubes = {}
    for y, line in enumerate(read_file()):
        for x, c in enumerate(line):
            cubes[(x, y, 0, 0)] = HyperCube((x, y, 0, 0), c)

    for i in range(6):
        # create neighbours if necesary
        needed_cubes = set()
        for cube in cubes.values():
            if cube.active:
                needed_cubes |= set(cube.get_neighbours())
        for position in needed_cubes:
            if not position in cubes:
                cubes[position] = HyperCube(position, False)

        # recount all neighbours
        for cube in cubes.values():
            cube.recount()
        for cube in cubes.values():
            if cube.active:
                for position in cube.get_neighbours():
                    cubes[position].active_neighbour_count += 1

        # check activation
        for cube in cubes.values():
            cube.check_activation()

    print(len([cube for cube in cubes.values() if cube.active]))





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









