#! /usr/bin/python
import sys, getopt

def parse_input( lines ):
    left = []
    right = []
    for line in read_file():
        l, r = map( int, line.split())
        left.append(l)
        right.append(r)
    return left, right

def solve_star1():
    left, right = parse_input( read_file() )
    left = sorted( left )
    right = sorted( right )
    return sum( abs( l - r ) for (l,r) in zip( left, right ) )

def solve_star2():
    left, right = parse_input( read_file() )
    return sum( v * right.count( v ) for v in left )


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
