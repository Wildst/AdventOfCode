#! /usr/bin/python
import sys, getopt

DIRECTIONS = "NESW"
DIRECTION_DIFFS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def solve_star1():
    x, y, direction = 0, 0, 1

    for instruction in read_file():
        amount = int(instruction[1:])
        if instruction[0] in "LR":
            direction += -1*(amount//90) if instruction[0] == "L" else 1*(amount//90)
            direction %= 4
        else:
            dx, dy = DIRECTION_DIFFS[direction] if instruction[0] == "F" else DIRECTION_DIFFS[DIRECTIONS.index(instruction[0])]
            x += dx * amount
            y += dy * amount
    print(abs(x) + abs(y))

def solve_star2():
    ship_x, ship_y = 0, 0
    waypoint_x, waypoint_y = 10, -1

    for instruction in read_file():
        amount = int(instruction[1:])
        if instruction[0] in "LR":
            for _ in range((amount if instruction[0] == "L" else 360 - amount)//90):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif instruction[0] == "F":
            ship_x += waypoint_x * amount
            ship_y += waypoint_y * amount
        else:
            dx, dy = DIRECTION_DIFFS[DIRECTIONS.index(instruction[0])]
            waypoint_x += dx * amount
            waypoint_y += dy * amount
    print(abs(ship_x) + abs(ship_y))



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









