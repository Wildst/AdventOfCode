#! /usr/bin/python
import sys, getopt
from copy import deepcopy

def area_to_string(area):
    return "\n".join("".join(row) for row in area)

def adjacent_occupied_seat_count(area, pos):
    x, y = pos
    return sum("".join(area[row][x-1:x+2]).count("#") for row in range(y-1, y+2) )


def solve_star1():
    area = [[".", *row, "."] for row in read_file()]
    area = [["." for _ in area[0]], *area, ["." for _ in area[0]]]
    changed = True
    while changed:
        changed = False
        old = deepcopy(area)
        for i, row in enumerate(area[1:-1]):
            for j, seat in enumerate(row[1:-1]):
                if seat == "L":
                    if adjacent_occupied_seat_count(old, (j+1, i+1)) == 0:
                        row[j+1] = "#"
                        changed = True
                elif seat == "#":
                    if adjacent_occupied_seat_count(old, (j+1, i+1)) >= 5:
                        row[j+1] = "L"
                        changed = True
    print(area_to_string(area).count("#"))


def visible_occupied_seat_count(area, pos):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]
    count = 0
    for direction in directions:
        x, y = pos
        dx, dy = direction
        x, y = x+dx, y+dy
        while 0 <= x < len(area) and 0 <= y < len(area[0]) and area[x][y] == ".":
            x, y = x+dx, y+dy

        if 0 <= x < len(area) and 0 <= y < len(area[0]):
            if area[x][y] == "#":
                count += 1
    return count

def solve_star2():
    area = [[*row] for row in read_file()]
    changed = True
    while changed:
        changed = False
        old = deepcopy(area)
        for i, row in enumerate(area):
            for j, seat in enumerate(row):
                if seat == "L":
                    if visible_occupied_seat_count(old, (i, j)) == 0:
                        row[j] = "#"
                        changed = True
                elif seat == "#":
                    if visible_occupied_seat_count(old, (i, j)) >= 5:
                        row[j] = "L"
                        changed = True
    print(area_to_string(area).count("#"))


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









