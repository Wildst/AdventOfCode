#! /usr/bin/python
import sys, getopt

directions = {
    "R": ( 1, 0),
    "U": ( 0, 1),
    "L": (-1, 0),
    "D": ( 0,-1)
}

def follow(h, t):
    has_to_move = abs(h[0]-t[0]) > 1 or abs(h[1]-t[1]) > 1
    before = h, t
    if h[0] != t[0] and has_to_move:
        t = t[0] - (1 if t[0] > h[0] else -1),t[1]
    if h[1] != t[1] and has_to_move:
        t = t[0], t[1] - (1 if t[1] > h[1] else -1)
    return t

def solve_star1():
    h = t = 0,0
    positions = set()
    positions.add(t)
    for line in read_file():
        direction, amount = line.split()
        dx, dy = directions[direction]
        for _ in range(int(amount)):
            h = h[0]+dx, h[1]+dy
            t = follow(h, t)
            positions.add(t)
    return len(positions)

def solve_star2():
    rope = [(0,0) for _ in range(10)]
    positions = set()
    positions.add(rope[-1])
    for line in read_file():
        direction, amount = line.split()
        dx, dy = directions[direction]
        for _ in range(int(amount)):
            rope[0] = rope[0][0]+dx, rope[0][1]+dy
            for i in range(9):
                rope[i+1] = follow(rope[i], rope[i+1])
            positions.add(rope[-1])
    return len(positions)


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
