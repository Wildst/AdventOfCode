#! /usr/bin/python
import sys, getopt

DIRECTIONS = [
    ( 1, 0 ),
    ( 0,-1 ),
    (-1, 0 ),
    ( 0, 1 )
]

def parse_input( data ):
    walls = set()
    start = (-1, -1)
    end = (-1, -1)
    for y, line in enumerate( data ):
        for x, element in enumerate( line ):
            if element == "#":
                walls.add( ( x, y ) )
            elif element == "E":
                end = ( x, y )
            elif element == "S":
                start = ( x, y )
    return start, end, walls

def get_direction_change_cost( direction_1, direction_2 ):
    if direction_1 == direction_2:
        return 0
    elif abs( direction_1 - direction_2 ) == 2:
        return 2000
    else:
        return 1000

def get_values( walls, start ):
    checks = set( ( start, i ) for i in range( len( DIRECTIONS ) ) )
    values = {}
    values[ start ] = [ 0, 1000, 2000, 1000 ]
    while checks:
        position, direction = checks.pop()

        # Move forward
        dx, dy = DIRECTIONS[ direction ]
        x, y = position
        next_position = x+dx, y+dy
        if next_position not in walls:
            if next_position not in values:
                values[ next_position ] = [ values[position][direction] + 1 + get_direction_change_cost( direction, i ) for i in range( len( DIRECTIONS ) ) ]
                for i in range( len( DIRECTIONS ) ):
                    checks.add( ( next_position, i) )
            else:
                if values[ next_position ][ direction ] > values[ position ][ direction ] + 1:
                    values[ next_position ][ direction ] = values[ position ][ direction ] + 1
                    checks.add( (next_position, direction) )

        # turns
        if values[ position ][ (direction-1)%4 ] > values[ position ][ direction ] + 1000:
            values[ position ][ (direction-1)%4 ] = values[ position ][ direction ] + 1000
            checks.add( (position, (direction-1)%4) )

        if values[ position ][ (direction+1)%4 ] > values[ position ][ direction ] + 1000:
            values[ position ][ (direction+1)%4 ] = values[ position ][ direction ] + 1000
            checks.add( (position, (direction+1)%4) )
    return values


def solve_star1():
    start, end, walls = parse_input( read_file() )
    values = get_values( walls, start)
    return min( values[ end ] )

def solve_star2():
    start, end, walls = parse_input( read_file() )
    values = get_values( walls, start )

    path_positions = set()
    checks = set()
    for i, value in enumerate( values[ end ] ):
        if value == min( values[ end ] ):
            checks.add( ( end, i ) )
    while checks:
        position, direction = checks.pop()
        path_positions.add( position )

        # Move bacx
        dx, dy = DIRECTIONS[ direction ]
        x, y = position
        previous_position = x-dx, y-dy
        if previous_position not in walls:
            if values[ previous_position ][ direction ] == values[ position ][ direction ] - 1:
                checks.add( (previous_position, direction) )

        # turns
        if values[ position ][ (direction-1)%4 ] == values[ position ][ direction ] - 1000:
            checks.add( (position, (direction-1)%4) )

        if values[ position ][ (direction+1)%4 ] == values[ position ][ direction ] - 1000:
            checks.add( (position, (direction+1)%4) )
    return len( path_positions )


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
