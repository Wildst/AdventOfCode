#! /usr/bin/python
import sys, getopt

DIRECTIONS = [
    (  1,  0 ),
    (  1,  1 ),
    (  0,  1 ),
    ( -1,  1 ),
    ( -1,  0 ),
    ( -1, -1 ),
    (  0, -1 ),
    (  1, -1 )]

DIAGONALS = [
    (  1,  1 ),
    ( -1,  1 ),
    ( -1, -1 ),
    (  1, -1 )]

def is_valid( pos, grid ):
    x, y = pos
    return 0<= x < len( grid[0] ) and 0<=y< len(grid)

def is_xmas( startpos, grid, direction ):
    x, y = startpos
    dx, dy = direction
    for i,c in enumerate( "XMAS" ):
        new_x, new_y = x + dx*i, y+ dy*i
        if not is_valid( (new_x,new_y), grid ) or grid[ new_y ][ new_x ] != c:
            return False
    return True
def solve_star1():
    grid = read_file()
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for direction in DIRECTIONS:
                if is_xmas( (x, y), grid, direction ):
                    result += 1
    return result

def is_x_mas( pos, grid ):
    x, y = pos
    if grid[y][x] != "A":
        return False
    count = 0
    for dx, dy in DIAGONALS:
        if grid[y-dy][x-dx] == "M" and grid[y+dy][x+dx] == "S":
            count += 1
    return count == 2

def solve_star2():
    grid = read_file()
    result = 0
    for y in range(1,len(grid)-1):
        for x in range(1,len(grid[0])-1):
            if is_x_mas( (x, y), grid ):
                result += 1
    return result


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
