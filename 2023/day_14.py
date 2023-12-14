#! /usr/bin/python
import sys, getopt

north = (0, -1)
east = (1, 0)
south = (0, 1)
west = (-1, 0)

def roll_up( rock, placed_rocks ):
    x, y = rock
    while y > 0 and (x, y - 1) not in placed_rocks:
        y -= 1
    return x, y

def roll( movable_rocks, solid_rocks, direction, bounds ):
    max_x, max_y = bounds
    new_movable_positions = set()
    dx, dy = direction
    while movable_rocks:
        rock_count = 1
        x, y = movable_rocks.pop()
        while 0 <= y + dy < max_y and 0 <= x + dx < max_x and ( x + dx, y + dy ) not in solid_rocks and (x + dx, y+dy ) not in new_movable_positions:
            x, y = x + dx, y + dy
            if (x, y) in movable_rocks:
                movable_rocks.remove( (x, y ) )
                rock_count += 1
        for i in range( rock_count ):
            new_movable_positions.add( ( x - i*dx, y - i *dy ) )
    return new_movable_positions

def solve_star1():
    platform = read_file()

    placed_rocks = set()
    load = 0

    for y, line in enumerate( platform ):
        for x, rock in enumerate( line ):
            if rock == "O":
                final_pos = roll_up( (x, y), placed_rocks )
                load += len( platform ) - final_pos[ 1 ]
                placed_rocks.add( final_pos )
            if rock == "#":
                placed_rocks.add( ( x, y ) )
    return load


def find_rocks( platform ):
    solid_rocks = set()
    movable_rocks = set()

    for y, line in enumerate( platform ):
        for x, rock in enumerate( line ):
            if rock == "O":
                movable_rocks.add( ( x, y ) )
            elif rock == "#":
                solid_rocks.add( ( x, y ) )
    return movable_rocks, solid_rocks

def get_hash( movable_rocks ):
    return hash( "".join(sorted( ["(%i,%i)" %(x,y) for x, y in movable_rocks] )))

def do_cycle( movable_rocks, solid_rocks, bounds ):
    for direction in [north, west, south, east]:
        movable_rocks = roll( movable_rocks, solid_rocks, direction, bounds )
    return movable_rocks

def solve_star2():
    platform = read_file()
    bounds = (len(platform[ 0 ]), len(platform))
    movable_rocks, solid_rocks = find_rocks( platform )
    previous_positions = []
    h = get_hash( movable_rocks )
    while h not in previous_positions:
        previous_positions.append( h )
        movable_rocks = do_cycle( movable_rocks, solid_rocks, bounds )
        h = get_hash( movable_rocks )
    cycle_len = len( previous_positions ) - previous_positions.index( h )
    for _ in range( ( 1000000000 - len( previous_positions ) ) % cycle_len ):
        movable_rocks = do_cycle( movable_rocks, solid_rocks, bounds )

    return sum(bounds[1] - y for x,y in movable_rocks)


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
