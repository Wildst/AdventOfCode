#! /usr/bin/python3.8
import sys, getopt
from functools import reduce

def get_adjacent(x, y, h, w):
    opts = []
    if x > 0:
        opts.append((x-1,y))
    if y > 0:
        opts.append((x,y-1))
    if x < w-1:
        opts.append((x+1, y))
    if y < h-1:
        opts.append((x, y+1))

    return opts

def solve_star1():
    points = [[int(c) for c in line] for line in read_file()]
    h = len(points)
    w = len(points[0])
    risk = 0
    for y, row in enumerate(points):
        for x, point in enumerate(row):
            if min(map(lambda a: points[a[1]][a[0]], get_adjacent(x,y,h,w))) > point:
                risk += point+1
    return risk

def calc_basin_size(points, x, y, h, w):
    basin = set()
    todo = set()
    todo.add((x,y))
    while todo:
        point = todo.pop()
        if point not in basin:
            basin.add(point)
            for p in get_adjacent(point[0], point[1], h, w):
                if points[p[1]][p[0]] != 9:
                    todo.add(p)
    return len(basin)


def solve_star2():
    points = [[int(c) for c in line] for line in read_file()]
    h = len(points)
    w = len(points[0])
    basins = []
    for y, row in enumerate(points):
        for x, point in enumerate(row):
            if min(map(lambda a: points[a[1]][a[0]], get_adjacent(x,y,h,w))) > point:
                basins.append(calc_basin_size(points, x, y, h, w))
    return reduce(lambda a,b: a*b, sorted(basins)[-3:])



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
