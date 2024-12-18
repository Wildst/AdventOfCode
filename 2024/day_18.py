#! /usr/bin/python
import sys, getopt

DIRECTIONS = [
    ( 1, 0 ),
    ( 0, 1 ),
    (-1, 0 ),
    ( 0,-1 )
]

def is_valid( pos ):
    x, y = pos
    return 0 <= x <= max_coord and 0 <= y <= max_coord

def solve_star1():
    coordinates = [ tuple( map( int, line.split(",") ) ) for line in read_file()][:fall_limit]
    distances = [ [ max_coord * max_coord for _ in range( max_coord + 1 ) ] for _ in range( max_coord + 1 ) ]
    distances[ 0 ][ 0 ] = 0

    todo = set()
    todo.add( ( 0, 0 ) )
    while todo:
        x, y = todo.pop()
        for dx, dy in DIRECTIONS:
            if not is_valid( ( x+dx, y+dy ) ) or ( x+dx, y+dy ) in coordinates:
                continue
            if distances[ y ][ x ] + 1 < distances[ y+dy ][ x+dx ]:
                todo.add( (x+dx, y+dy) )
                distances[ y+dy ][ x+dx ] = distances[ y ][ x ] + 1

    return distances[ max_coord ][ max_coord ]

def can_reach( coordinates ):
    distances = [ [ max_coord * max_coord for _ in range( max_coord + 1 ) ] for _ in range( max_coord + 1 ) ]
    distances[ 0 ][ 0 ] = 0

    todo = set()
    todo.add( ( 0, 0 ) )
    while todo:
        x, y = todo.pop()
        for dx, dy in DIRECTIONS:
            if not is_valid( ( x+dx, y+dy ) ) or ( x+dx, y+dy ) in coordinates:
                continue
            if distances[ y ][ x ] + 1 < distances[ y+dy ][ x+dx ]:
                todo.add( (x+dx, y+dy) )
                distances[ y+dy ][ x+dx ] = distances[ y ][ x ] + 1

    return distances[ max_coord ][ max_coord ] < max_coord * max_coord


def solve_star2():
    coordinates = [ tuple( map( int, line.split(",") ) ) for line in read_file()]
    for i, coordinate in enumerate( coordinates ):
        if not can_reach( coordinates[:i+1]):
            return ",".join( map( str, coordinate ) )


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
    max_coord = 70
    fall_limit = 1024

    for opt, arg in opts:
        if opt == "-i":
            infile = arg
        elif opt == "-1":
            star = 1
        elif opt == "-2":
            star = 2
        if opt == "-t":
            max_coord = 6
            fall_limit = 12
            file_dir = "test_files"

    if star == 1:
        print(solve_star1())
    elif star == 2:
        print(solve_star2())
