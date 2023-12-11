#! /usr/bin/python
import sys, getopt

def all_zeros( sequence ):
    for i in sequence:
        if i:
            return False
    return True

def get_differences( sequence ):
    result = []
    for i in range( len( sequence ) - 1 ):
        result.append( sequence[ i + 1 ] - sequence[ i ] )
    return result

def get_next( sequence ):
    differences = get_differences( sequence )
    if all_zeros( sequence ):
        return 0
    else:
        return sequence[ -1 ]+ get_next( differences )

def get_previous( sequence ):
    differences = get_differences( sequence )
    if all_zeros( sequence ):
        return 0
    else:
        return sequence[ 0 ] - get_previous( differences )

def solve_star1():
    result = 0
    for line in read_file():
        sequence = [ *map( int, line.split() ) ]
        result += get_next( sequence )
    return result


def solve_star2():
    result = 0
    for line in read_file():
        sequence = [ *map( int, line.split() ) ]
        result += get_previous( sequence )
    return result


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
