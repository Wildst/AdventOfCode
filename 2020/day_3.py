#! /usr/bin/python
import sys, getopt

def slide_down(forest, direction):
    (dx, dy) = direction
    trees = 0
    x = 0
    y = 0
    while y < len(forest):
        row = forest[y]
        if row[x % len(row)] == "#":
            trees += 1
        x += dx
        y += dy
    return trees

def solve_star1():
    forest = read_file()
    print(slide_down(forest, (3, 1)))


def solve_star2():
    forest = read_file()
    directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    encounters = [slide_down(forest, direction) for direction in directions]

    solution = 1
    for encounter in encounters:
        solution *= encounter
    
    print(solution)


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









