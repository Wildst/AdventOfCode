#! /usr/bin/python3.8
import sys, getopt

def get_directions(x, y, max_x, max_y):
    dirs = []
    if x > 0:
        dirs.append((x-1,y))
    if y > 0:
        dirs.append((x,y-1))
    if x+1 < max_x:
        dirs.append((x+1,y))
    if y+1 < max_y:
        dirs.append((x,y+1))
    return dirs

def solve_star1():
    risks = [[*map(int, line)] for line in read_file()]
    costs = [[-1 for _ in line] for line in read_file()]
    costs[0][0] = 0
    updated = set()
    updated.add((0, 0))
    i = 0
    while updated:
        x,y = updated.pop()
        for x2, y2 in get_directions(x,y, len(risks[0]), len(risks)):
            test = costs[y][x] + risks[y2][x2]
            if test < costs[y2][x2] or costs[y2][x2] < 0:
                costs[y2][x2] = test
                updated.add((x2,y2))
    return costs[-1][-1]

def get_risk(base_risks, x, y):
    x_off = x//len(base_risks[0])
    y_off = y//len(base_risks)
    x_in = x%len(base_risks[0])
    y_in = y%len(base_risks[0])
    risk = base_risks[y_in][x_in] + x_off + y_off
    return risk if risk < 10 else risk - 9

def solve_star2():
    base_risks = [[*map(int, line)] for line in read_file()]
    costs = [[-1 for _ in range(len(base_risks[0])*5)] for _ in range(len(base_risks)*5)]
    costs[0][0] = 0
    updated = set()
    updated.add((0, 0))
    i = 0
    while updated:
        x,y = updated.pop()
        for x2, y2 in get_directions(x,y, len(base_risks[0])*5, len(base_risks)*5):
            test = costs[y][x] + get_risk(base_risks, x2, y2)
            if test < costs[y2][x2] or costs[y2][x2] < 0:
                costs[y2][x2] = test
                updated.add((x2,y2))
    return costs[-1][-1]


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
