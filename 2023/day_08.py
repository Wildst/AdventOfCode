#! /usr/bin/python
import sys, getopt

def solve_star1():
    lines = read_file()

    nodes = {}
    for line in lines[2:]:
        start, directions = line.split(" = ")
        left, right = directions[1:-1].split(", ")
        nodes[ start ] = (left, right)

    directions = lines[0]

    steps = 0
    node = "AAA"
    while node != "ZZZ":
        node = nodes[ node ][0 if directions[steps % len(directions)] == "L" else 1]
        steps += 1
    return steps

def solve_star2():
    lines = read_file()

    ghosts = set()

    nodes = {}
    for line in lines[2:]:
        start, directions = line.split(" = ")
        left, right = directions[1:-1].split(", ")
        nodes[ start ] = (left, right)
        if start.endswith("A"):
            ghosts.add( start )

    directions = lines[0]

    repeats = []
    for ghost in ghosts:
        steps = 0
        while not ghost.endswith("Z"):
            ghost = nodes[ ghost ][ 0 if directions[ steps % len(directions) ] == "L" else 1 ]
            steps += 1
        repeats.append( steps )

    step = 1
    for interval in repeats:
        current = step
        while current % interval:
            current += step
        step = current
    return step


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
