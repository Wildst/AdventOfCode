#! /usr/bin/python
import sys, getopt

DIRECTIONS = {
    ( 1, 0 ),
    ( 1, 1 ),
    ( 0, 1 ),
    (-1, 1 ),
    (-1, 0 ),
    (-1,-1 ),
    ( 0,-1 ),
    ( 1,-1 )
}

def animate( lights ):
    new_lights = []
    for y, line in enumerate( lights ):
        new_line = ""
        for x, state in enumerate( line ):
            count = 0
            for dx, dy in DIRECTIONS:
                if 0 <= x+dx < len( line ) and 0 <= y+dy < len( lights ) and lights[ y+dy ][ x+dx ] == "#":
                    count += 1
            if state == "#":
                new_line += "#" if 2 <= count <= 3 else "."
            else:
                new_line += "#" if count == 3 else "."
        new_lights.append( new_line )
    return new_lights


def solve_star1():
    lights = read_file()
    for _ in range( steps ):
        lights = animate( lights )
    return "".join( lights ).count( "#")

def solve_star2():
    lights = read_file()
    for _ in range( steps ):
        lights = animate( lights )
        lights[ 0 ] = "#" + lights[ 0 ][ 1:-1 ] + "#"
        lights[ -1 ] = "#" + lights[ -1 ][ 1:-1 ] + "#"
    return "".join( lights ).count( "#")


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
    steps = 100

    for opt, arg in opts:
        if opt == "-i":
            infile = arg
        elif opt == "-1":
            star = 1
        elif opt == "-2":
            star = 2
        if opt == "-t":
            file_dir = "test_files"
            steps = 4

    if star == 1:
        print(solve_star1())
    elif star == 2:
        if steps == 4:
            steps = 5
        print(solve_star2())
