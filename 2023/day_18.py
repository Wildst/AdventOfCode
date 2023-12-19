#! /usr/bin/python
import sys, getopt

directions = {
    "U": ( 0, -1),
    "R": ( 1,  0),
    "D": ( 0,  1),
    "L": (-1,  0)
}

def in_grid( pos, grid ):
    x, y = pos
    return 0 <= x < len( grid[ 0 ] ) and 0 <= y < len( grid )

def solve_star1():
    x = 0
    y = 0
    corners = [(x,y)]
    for line in read_file():
        direction, amount, _ = line.split()
        dx, dy = directions[ direction]
        x += dx * int( amount )
        y += dy * int( amount )
        corners.append( (x, y))

    s = 0
    for i in range( len( corners ) ):
        # inner part
        s += corners[ i - 1 ][ 0 ] * corners[ i ][ 1 ]
        s -= corners[ i - 1 ][ 1 ] * corners[ i ][ 0 ]
        # border
        s += abs( corners[ i - 1 ][ 0 ] - corners[ i ][ 0 ])
        s += abs( corners[ i - 1 ][ 1 ] - corners[ i ][ 1 ])
    s //= 2

    # last corner
    s += 1
    return s

def solve_star2():
    x = 0
    y = 0
    corners = [(x,y)]
    for line in read_file():
        _, _, h = line.split()
        h = h[2:-1]
        amount = int(h[:-1], 16)
        direction = "RDLU"[int( h[-1])]
        dx, dy = directions[ direction ]
        x += amount * dx
        y += amount * dy
        corners.append( (x, y))

    s = 0
    for i in range( len( corners ) ):
        # inner part
        s += corners[ i - 1 ][ 0 ] * corners[ i ][ 1 ]
        s -= corners[ i - 1 ][ 1 ] * corners[ i ][ 0 ]
        # border
        s += abs( corners[ i - 1 ][ 0 ] - corners[ i ][ 0 ])
        s += abs( corners[ i - 1 ][ 1 ] - corners[ i ][ 1 ])
    s //= 2

    # last corner
    s += 1
    return s

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
