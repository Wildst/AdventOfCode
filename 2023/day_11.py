#! /usr/bin/python
import sys, getopt

def expand( galaxy ):
    for i in range( len(galaxy) - 1, -1, -1 ):
        if galaxy[ i ].count( "#" ) == 0:
            galaxy = galaxy[ :i ] + [ galaxy[ i ] ] + galaxy[ i: ]
    for i in range( len(galaxy[0]) -1, -1, -1 ):
        if len( [ 1 for row in galaxy if row[ i ] == '#' ] ) == 0:
            galaxy = [ row[ :i ] + row[ i ] + row[ i: ] for row in galaxy ]
    return galaxy

def find_stars( galaxy ):
    stars = []
    for y, row in enumerate( galaxy ):
        for x, space in enumerate( row ):
            if space == "#":
                stars.append( (x, y) )
    return stars

def find_expansion_lines( galaxy ):
    rows = []
    columns = []
    for i in range( len(galaxy) - 1, -1, -1 ):
        if galaxy[ i ].count( "#" ) == 0:
            rows.append( i )
    for i in range( len(galaxy[0]) -1, -1, -1 ):
        if len( [ 1 for row in galaxy if row[ i ] == '#' ] ) == 0:
            columns.append( i )
    return rows, columns


def solve_star1():
    galaxy = expand( read_file() )
    stars = find_stars( galaxy )
    total_distance = 0
    for i, star in enumerate( stars ):
        x1, y1 = star
        for other_star in stars[:i]:
            x2, y2 = other_star
            total_distance += abs( x2 - x1 ) + abs( y2 - y1 )
    return total_distance

def solve_star2( testing = False ):
    expansion_rate = 100 if testing else 1000000
    galaxy = read_file()
    stars = find_stars( galaxy )
    rows, columns = find_expansion_lines( galaxy )

    total_distance = 0
    for i, star in enumerate( stars ):
        x1, y1 = star
        for other_star in stars[:i]:
            x2, y2 = other_star
            expansion_factor = len( [ x for x in columns if min( x1, x2 ) < x < max( x1, x2 ) ])
            expansion_factor += len( [ y for y in rows if min( y1, y2 ) < y < max( y1, y2 ) ])
            total_distance += abs( x2 - x1 ) + abs( y2 - y1 ) + ( expansion_rate - 1 ) * expansion_factor
    return total_distance


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][0:-2] + "in"
    file_dir = "input_files"
    star = 1
    testing = False

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
            testing = True
            file_dir = "test_files"

    if star == 1:
        print(solve_star1())
    elif star == 2:
        print(solve_star2( testing ))
