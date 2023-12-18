#! /usr/bin/python
import sys, getopt

up = (0, -1)
right = (1, 0)
down = (0, 1)
left = (-1, 0)
directions = [up, right, down, left]

def in_grid( pos, grid ):
    x, y = pos
    return 0 <= x < len( grid[0] ) and 0 <= y < len( grid )

def move_beam( beam, grid ):
    pos, direction = beam
    x,y = pos
    dx, dy = direction
    x, y = x+dx, y+dy
    if not in_grid( (x,y), grid ):
        return []

    if grid[y][x] == ".":
        return [((x, y), direction)]
    elif grid[ y ][ x ] == "/":
        if direction == left:
            return [((x, y), down)]
        elif direction == down:
            return [((x,y), left)]
        elif direction == right:
            return [((x,y), up)]
        else:
            return [((x,y), right)]
    elif grid[ y ][ x ] == "\\":
        if direction == left:
            return [((x, y), up)]
        elif direction == down:
            return [((x,y), right)]
        elif direction == right:
            return [((x,y), down)]
        else:
            return [((x,y), left)]
    elif grid[ y ][x] == "-":
        if direction == up or direction == down:
            return [((x,y), left), ((x,y), right)]
        else:
            return [((x,y), direction)]
    else:
        if direction == right or direction == left:
            return [((x,y), down), ((x,y), up)]
        else:
            return[((x,y), direction)]

def get_beam_char( pos, beams ):
    c = 0
    direction = right
    for p, d in beams:
        if pos != p:
            continue
        c += 1
        direction = d
    if c == 0:
        return "."
    if c == 1:
        if direction == right:
            return ">"
        elif direction == left:
            return "<"
        elif direction == up:
            return "^"
        elif direction == down:
            return "v"
    else:
        return str( c )

def get_beam_value( start, grid ):
    all_beams = set()
    beams_to_check = [start]
    while beams_to_check:
        beam = beams_to_check[ 0 ]
        beams_to_check = beams_to_check[1:]
        if beam in all_beams:
            continue
        all_beams.add( beam )
        for next in move_beam( beam, grid ):
            beams_to_check.append( next )

    energized = set( pos for pos, _ in all_beams if in_grid( pos, grid ))
    return len(energized)



def solve_star1():
    grid = read_file()
    return get_beam_value( ( (-1, 0), right ), grid )

def solve_star2():
    best = 0
    grid = read_file()
    for x in range( len( grid[ 0 ] ) ):
        best = max( best, get_beam_value( ( ( x, -1 ), down ), grid ), get_beam_value( ((x, len( grid )), up), grid) )
    for y in range( len( grid ) ):
        best = max( best, get_beam_value( ( ( -1, y ), right ), grid ), get_beam_value( ((len( grid[ 0 ]), y), left), grid) )
    return best


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
