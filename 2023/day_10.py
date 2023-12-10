#! /usr/bin/python
import sys, getopt

north = 0, -1
east = 1, 0
south = 0, 1
west = -1, 0


pipes = {
    "|": [ north, south ],
    "-": [ east, west ],
    "L": [ north, east ],
    "J": [ north, west ],
    "7": [ south, west ],
    "F": [ south, east ],
    ".": [],
    "S": [ north, east, south, west ]
}

def expand_grid( grid ):
    result = [ "." + line + "." for line in grid ]
    result = ["." * len(result[ 0 ])] + result +[ "." * len(result[ 0 ]) ]
    return result

def find_start( grid ):
    for y, line in enumerate( grid ):
        for x, token in enumerate( line ):
            if token == "S":
                return x, y

def move( grid, pos, previous_pos ):
    x, y = pos
    pipe = grid[ y ][ x ]
    origin = previous_pos[ 0 ] - x, previous_pos[ 1 ] - y
    next_options = []
    found_origin = False
    for direction in pipes[ pipe ]:
        if direction != origin:
            next_options.append( ( x + direction[ 0 ], y + direction[ 1 ] ) )
        else:
            found_origin = True
    return next_options if found_origin else []

def found_loop(feelers):
    return len( feelers ) > len( set( pos for pos, _ in feelers ) )

def solve_star1():
    grid = expand_grid( read_file() )
    x, y = find_start( grid )
    counter = 1
    feelers = [ ( (x+dx, y+dy), (x, y) ) for dx, dy in pipes[ "S" ] ]
    while not found_loop(feelers):
        next_feelers = []
        for pos, prev_pos in feelers:
            for next_pos in move( grid, pos, prev_pos ):
                next_feelers.append( ( next_pos, pos ) )
        feelers = next_feelers

        counter += 1

    return counter


def solve_star2():
    return read_file()


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
