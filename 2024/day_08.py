#! /usr/bin/python
import sys, getopt

def get_antennas( data ):
    antennas = {}
    for y, row in enumerate( data ):
        for x, content in enumerate( row ):
            if content != ".":
                if content not in antennas:
                    antennas[ content ] = []
                antennas[ content ].append( (x,y) )
    return antennas

def solve_star1():
    field = read_file()
    antennas = get_antennas( field )
    antidotes = set()
    for antenna in antennas:
        locations = antennas[ antenna ]
        for i, pos_a in enumerate( locations[ :-1] ):
            for pos_b in locations[i+1:]:
                x_a, y_a = pos_a
                x_b, y_b = pos_b
                dx, dy = x_a - x_b, y_a - y_b
                antidotes.add( (x_a +dx, y_a + dy) )
                antidotes.add( (x_b -dx, y_b - dy) )
    return len( [ (x,y) for x,y in antidotes if 0 <= x < len( field[ 0] ) and 0 <= y < len( field ) ] )

def is_valid( location, field ):
    x,y = location
    return 0 <= x < len( field[0]) and 0 <= y <= len( field )

def simplify_direction( x, y ):
    i = 2
    while i < x:
        if x % i or y % i:
            i += 1
        else:
            x = x // i
            y = y // i
    return x, y

def solve_star2():
    field = read_file()
    antennas = get_antennas( field )
    antidotes = set()
    for antenna in antennas:
        locations = antennas[ antenna ]
        for i, pos_a in enumerate( locations[ :-1] ):
            for pos_b in locations[i+1:]:
                x_a, y_a = pos_a
                x_b, y_b = pos_b
                dx, dy = simplify_direction( x_a - x_b, y_a - y_b )
                j = 0
                while is_valid( ( x_a + j*dx, y_a + j*dy ), field ):
                    antidotes.add( ( x_a + j*dx, y_a + j*dy ) )
                    j += 1
                j = 0
                while is_valid( ( x_b - j*dx, y_b - j*dy ), field ):
                    antidotes.add( ( x_b - j*dx, y_b - j*dy ) )
                    j += 1
    return len( [ (x,y) for x,y in antidotes if 0 <= x < len( field[ 0] ) and 0 <= y < len( field ) ] )



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
