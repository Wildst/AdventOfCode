#! /usr/bin/python
import sys, getopt

directions = {(0,1), (-1,0), (0,-1), (1, 0)}

def to_height(char):
    if char == "S":
        return 0
    if char == "E":
        return 25
    else:
        return ord(char) - ord("a")


def solve_star1():
    heigth_map = [[to_height(char) for char in line] for line in read_file()]
    moves = [[len(heigth_map)*len(heigth_map[0]) for _ in line] for line in heigth_map]
    positions = set()
    start = "".join(read_file()).find("S")
    destination = "".join(read_file()).find("E")
    positions.add((start %len(heigth_map[0]), start // len(heigth_map[0])))
    moves[start//len(heigth_map[0])][start%len(heigth_map[0])] = 0
    while positions:
        check = positions.pop()
        for dx, dy in directions:
            if 0 <= check[0] + dx < len(heigth_map[0]) and 0 <= check[1]+dy < len(heigth_map):
                if heigth_map[check[1]][check[0]]+1 >= heigth_map[check[1]+dy][check[0]+dx]:
                    if moves[check[1]+dy][check[0]+dx] > moves[check[1]][check[0]] + 1:
                        moves[check[1]+dy][check[0]+dx] = moves[check[1]][check[0]] + 1
                        positions.add((check[0]+dx, check[1]+dy))
    return moves[destination//len(heigth_map[0])][destination%len(heigth_map[0])]

def solve_star2():
    heigth_map = [[to_height(char) for char in line] for line in read_file()]
    moves = [[len(heigth_map)*len(heigth_map[0]) for _ in line] for line in heigth_map]
    positions = set()
    destination = "".join(read_file()).find("E")
    for y, line in enumerate(heigth_map):
        for x, heigth in enumerate(line):
            if heigth == 0:
                moves[y][x] = 0
                positions.add((x,y))
    while positions:
        check = positions.pop()
        for dx, dy in directions:
            if 0 <= check[0] + dx < len(heigth_map[0]) and 0 <= check[1]+dy < len(heigth_map):
                if heigth_map[check[1]][check[0]]+1 >= heigth_map[check[1]+dy][check[0]+dx]:
                    if moves[check[1]+dy][check[0]+dx] > moves[check[1]][check[0]] + 1:
                        moves[check[1]+dy][check[0]+dx] = moves[check[1]][check[0]] + 1
                        positions.add((check[0]+dx, check[1]+dy))
    return moves[destination//len(heigth_map[0])][destination%len(heigth_map[0])]


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
