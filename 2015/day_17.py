#! /usr/bin/python
import sys, getopt

def fit( amount, barrels ):
    solutions = 0
    for i, barrel in enumerate( barrels ):
        if amount == barrel:
            solutions += 1
        elif amount > barrel:
            solutions += fit( amount - barrel, barrels[ i+1: ] )
    return solutions

def solve_star1():
    barrels = [ *map( int, read_file() ) ]
    return fit( target, barrels )

def fit_barrel_counts( amount, barrels ):
    solutions = [ 0 for _ in range( len( barrels ) + 1 ) ]
    for i, barrel in enumerate( barrels ):
        if amount == barrel:
            solutions[ 1 ] += 1
        elif amount > barrel:
            for i, count in enumerate( fit_barrel_counts( amount - barrel, barrels[ i+1: ] ) ):
                solutions[ i + 1 ] += count
    return solutions

def solve_star2():
    barrels = [ *map( int, read_file() ) ]
    for count in fit_barrel_counts( target, barrels ):
        if count > 0:
            return count


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

    target = 150

    for opt, arg in opts:
        if opt == "-i":
            infile = arg
        elif opt == "-1":
            star = 1
        elif opt == "-2":
            star = 2
        if opt == "-t":
            file_dir = "test_files"
            target = 25

    if star == 1:
        print(solve_star1())
    elif star == 2:
        print(solve_star2())
