#! /usr/bin/python3.8
import sys, getopt

directions = {
    "forward": [1, 0],
    "down": [0, 1],
    "up": [0, -1]
}

def solve_star1():
    x, y = 0,0
    for line in read_file():
        direction, amount = line.split()
        modifiers = directions[direction]
        amount = int(amount)
        x += amount * modifiers[0]
        y += amount * modifiers[1]
    return x*y


def solve_star2():
    aim, x, y = 0,0,0
    for line in read_file():
        direction, amount = line.split()
        modifiers = directions[direction]
        amount = int(amount)
        aim += amount * modifiers[1]
        x += amount * modifiers[0]
        y += amount * modifiers[0] * aim
    return x*y


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









