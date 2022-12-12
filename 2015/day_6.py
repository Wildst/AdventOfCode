#! /usr/bin/python
import sys, getopt

def solve_star1():
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in read_file():
        parts = line.split()
        start = [*map(int,parts[-3].split(','))]
        end = [*map(int, parts[-1].split(','))]
        if line.startswith("turn on"):
            for y in range(start[1], end[1] + 1):
                for x in range(start[0], end[0] + 1):
                    lights[y][x] = 1
        elif line.startswith("turn off"):
            for y in range(start[1], end[1] + 1):
                for x in range(start[0], end[0] + 1):
                    lights[y][x] = 0
        elif line.startswith("toggle"):
            for y in range(start[1], end[1] + 1):
                for x in range(start[0], end[0] + 1):
                    lights[y][x] = 1 - lights[y][x]
    return sum(sum(line) for line in lights)


def solve_star2():
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in read_file():
        parts = line.split()
        start = [*map(int,parts[-3].split(','))]
        end = [*map(int, parts[-1].split(','))]
        action = 0
        if line.startswith("turn on"):
            action = 1
        elif line.startswith("turn off"):
            action = -1
        elif line.startswith("toggle"):
            action = 2
        for y in range(start[1], end[1] + 1):
            for x in range(start[0], end[0] + 1):
                lights[y][x] = max(action + lights[y][x], 0)
    return sum(sum(line) for line in lights)


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
