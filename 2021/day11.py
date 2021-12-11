#! /usr/bin/python3.8
import sys, getopt

class Octopus():
    def __init__(self, energy_level, x, y):
        self.energy_level = energy_level
        self.x = x
        self.y = y

    def increase(self):
        self.energy_level += 1
        if self.energy_level == 10:
            return True
        return False

    def get_adjacent(self):
        return [(x,y) for x in range(max(0,self.x-1), min(10,self.x+2)) for y in range(max(0,self.y-1), min(10,self.y+2))]

    def calm_down(self):
        if self.energy_level > 9:
            self.energy_level = 0



def solve_star1():
    octopuses = []
    for y, line in enumerate(read_file()):
        octopuses.append([Octopus(int(c), x, y) for x, c in enumerate(line)])

    flashes = 0
    for i in range(100):
        todo = [(x,y) for x in range(10) for y in range(10)]
        for x, y in todo:
            octopus = octopuses[y][x]
            if octopus.increase():
                for other in octopus.get_adjacent():
                    todo.append(other)
                flashes += 1

        todo = [(x,y) for x in range(10) for y in range(10)]
        for x,y in todo:
            octopuses[y][x].calm_down()
    return flashes

def solve_star2():
    octopuses = []
    for y, line in enumerate(read_file()):
        octopuses.append([Octopus(int(c), x, y) for x, c in enumerate(line)])

    flashes = 0
    iteration = 0
    while flashes < 100:
        flashes = 0
        todo = [(x,y) for x in range(10) for y in range(10)]
        for x, y in todo:
            octopus = octopuses[y][x]
            if octopus.increase():
                for other in octopus.get_adjacent():
                    todo.append(other)
                flashes += 1

        todo = [(x,y) for x in range(10) for y in range(10)]
        for x,y in todo:
            octopuses[y][x].calm_down()
        iteration += 1
    return iteration


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
