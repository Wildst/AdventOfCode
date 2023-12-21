#! /usr/bin/python
import sys, getopt

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def find_start_pos( garden ):
    for y, row in enumerate( garden ):
        for x, tile in enumerate( row ):
            if tile == "S":
                return (x, y)

def in_garden( pos, garden ):
    x, y = pos
    return 0 <= x < len( garden[0] ) and 0 <= y < len( garden )

def print_options( garden, positions ):
    print( "\n".join( "".join( "O" if (x,y) in positions else tile for x, tile in enumerate( row ) ) for y, row in enumerate( garden ) ))

def move( garden, positions ):
    result = set()
    for x, y in positions:
        for dx, dy in directions:
            if in_garden( ( x+dx, y+dy ), garden ) and garden[ y+dy ][ x+dx ] != "#":
                result.add( (x+dx, y+dy) )
    return result

def solve_star1():
    garden = read_file()
    positions = set()
    positions.add( find_start_pos( garden ) )
    for _ in range( 64 ):
        positions = move( garden, positions )
    return len(positions)

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
