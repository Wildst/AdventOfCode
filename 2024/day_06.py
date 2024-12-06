#! /usr/bin/python
import sys, getopt

DIRECTIONS = [
    (  0, -1 ),
    (  1,  0 ),
    (  0,  1 ),
    ( -1,  0 )
]

def valid_pos( pos, ground ):
    x, y = pos
    return 0 <= x < len( ground[ 0 ] ) and 0 <= y < len( ground )

def find_pos( ground ):
    for y, row in enumerate( ground ):
        for x, place in enumerate( row ):
            if place == "^":
                return x, y
    return 0, 0

def get_next_pos( pos, direction ):
    x, y = pos
    dx, dy = direction
    return x + dx, y + dy

def can_walk( pos, ground ):
    if not valid_pos( pos, ground ):
        return True
    x, y = pos
    return ground[ y ][ x ] != "#"

def get_all_positions( start_pos, ground ):
    pos = start_pos
    direction = 0
    positions = set()
    while valid_pos( pos, ground ):
        positions.add( pos )
        next_pos = get_next_pos( pos, DIRECTIONS[ direction % len( DIRECTIONS ) ] )
        while not can_walk( next_pos, ground ):
            direction += 1
            next_pos = get_next_pos( pos, DIRECTIONS[ direction % len( DIRECTIONS ) ] )
        pos = next_pos
    return positions

def solve_star1():
    ground = read_file()
    pos = find_pos( ground )
    return len( get_all_positions( pos, ground ) )

def is_loop( ground, start_pos, obstacle ):
    direction = 0
    positions = set()
    if start_pos == obstacle:
        return False
    pos = start_pos
    while valid_pos( pos, ground ):
        if ( direction % len(DIRECTIONS), pos ) in positions:
            return True
        positions.add( ( direction % len(DIRECTIONS), pos ) )
        next_pos = get_next_pos( pos, DIRECTIONS[ direction % len( DIRECTIONS ) ] )
        while not can_walk( next_pos, ground ) or next_pos == obstacle:
            direction += 1
            next_pos = get_next_pos( pos, DIRECTIONS[ direction % len( DIRECTIONS ) ] )
        pos = next_pos
    return False


def solve_star2():
    ground = read_file()
    pos = find_pos( ground )
    return len( [ option for option in get_all_positions( pos, ground ) if is_loop( ground, pos, option ) ] )


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
