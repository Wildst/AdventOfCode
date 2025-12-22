#! /usr/bin/python
import sys, getopt

def parse_rolls(lines):
    rolls = set()
    for y, line in enumerate(lines):
        for x, pos in enumerate(line):
            if pos == "@":
                rolls.add((x,y))
    return rolls

def get_neighbour_positions(pos):
    x, y = pos
    neighbours = set()
    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx == 0 and dy == 0:
                continue
            neighbours.add((x+dx, y+dy))
    return neighbours

def get_neighbours(pos, grid):
    return get_neighbour_positions(pos).intersection(grid)


def solve_star1():
    rolls = parse_rolls(read_file())
    accessible = [roll for roll in rolls if len(get_neighbours(roll, rolls)) < 4 ]
    return len(accessible)
def solve_star2():
    rolls = parse_rolls(read_file())
    removed = 0
    accessible = set(roll for roll in rolls if len(get_neighbours(roll, rolls)) < 4)
    while accessible:
        removed += len(accessible)
        print( len(accessible) )
        for roll in accessible:
            rolls.remove(roll)
        accessible = set(roll for roll in rolls if len(get_neighbours(roll, rolls)) < 4)

    return removed


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
