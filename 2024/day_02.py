#! /usr/bin/python
import sys, getopt

def is_increasing( report ):
    return report == sorted( report )

def is_increasing_decreasing( report ):
    return is_increasing( report ) or is_increasing( report[::-1] )

def max_diff( report ):
    return max( abs( a - b ) for a, b in zip(report[:-1], report[1:] ) )

def min_diff( report ):
    return min( abs( a - b ) for a, b in zip(report[:-1], report[1:] ) )

def is_safe( report ):
    return is_increasing_decreasing( report ) and max_diff( report ) < 4 and min_diff( report ) > 0

def solve_star1():
    reports = [ [*map( int, line.split()) ] for line in read_file() ]
    return len( [r for r in reports if is_safe( r ) ] )

def is_almost_safe( report ):
    for i in range( len( report ) ):
        if is_safe( report[:i]+ report[ i+1:] ):
            return True
    return False

def solve_star2():
    reports = [ [*map( int, line.split()) ] for line in read_file() ]
    return len( [r for r in reports if is_almost_safe( r ) ] )


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
