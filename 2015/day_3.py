#! /usr/bin/python
import sys, getopt

directions={
    ">": (0,1),
    "<": (0,-1),
    "^": (1,0),
    "v":(-1,0)
}

def solve_star1():
    pos = (0,0)
    houses = set()
    houses.add(pos)
    for c in read_file()[0]:
        pos = pos[0] + directions[c][0], pos[1] + directions[c][1]
        houses.add(pos)
    return len(houses)
def solve_star2():
    p1 = (0,0)
    p2 = (0,0)
    houses = set()
    houses.add(p2)
    for i, c in enumerate(read_file()[0]):
        if i % 2:
            p1 = p1[0] + directions[c][0], p1[1] + directions[c][1]
            houses.add(p1)
        else:
            p2 = p2[0] + directions[c][0], p2[1] + directions[c][1]
            houses.add(p2)

    return len(houses)


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
