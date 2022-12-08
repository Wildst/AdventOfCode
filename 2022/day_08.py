#! /usr/bin/python
import sys, getopt
from functools import reduce

def solve_star1():
    trees = [[*map(int, [*row])] for row in read_file()]
    size = len(trees[0]), len(trees)
    max_heights = [[[-1,-1,-1,-1] for _ in range(size[0])] for _ in range(size[1])]

    for x in range(size[0]):
        for y in range(size[1]):
            neg_x = size[0]-x-1
            neg_y = size[1]-y-1

            if x > 0:
                # left
                max_heights[y][x][0] = max(max_heights[y][x-1][0], trees[y][x-1])
                # right
                max_heights[neg_y][neg_x][2] = max(max_heights[neg_y][neg_x+1][2], trees[neg_y][neg_x+1])
            if y > 0:
                # top
                max_heights[y][x][1] = max(max_heights[y-1][x][1], trees[y-1][x])
                # bottom
                max_heights[neg_y][neg_x][3] = max(max_heights[neg_y+1][neg_x][3], trees[neg_y+1][neg_x])

    return sum(len([1 for x in range(size[0]) if min(max_heights[y][x])<trees[y][x]]) for y in range(size[1]))


def solve_star2():
    trees = [[*map(int, [*row])] for row in read_file()]
    size = len(trees[0]), len(trees)
    vision = [[[0,0,0,0] for _ in range(size[0])] for _ in range(size[1])]
    for x in range(size[0]):
        for y in range(size[1]):
            # left
            if x > 0:
                px = x-1
                while px > 0 and trees[y][px] < trees[y][x]:
                    px -= 1
                vision[y][x][0] = x - px
            # top
            if y > 0:
                py = y-1
                while py > 0 and trees[py][x] < trees[y][x]:
                    py -= 1
                vision[y][x][1] = y - py
            # right
            if x+1 < size[0]:
                px = x+1
                while px+1 < size[0] and trees[y][px] < trees[y][x]:
                    px += 1
                vision[y][x][2] = px - x
            # bottom
            if y+1 < size[1]:
                py = y+1
                while py+1 < size[1] and trees[py][x] < trees[y][x]:
                    py += 1
                vision[y][x][3] = py - y
    return max(max(reduce(lambda a,b:a*b,vision[y][x]) for y in range(size[1])) for x in range(size[0]))


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
