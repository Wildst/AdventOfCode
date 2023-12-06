#! /usr/bin/python
import sys, getopt


def count_winning_options( time, distance ):
    for i in range( time ):
        if ( time - i ) * i > distance:
            return time - i * 2 + 1


def solve_star1():
    lines = read_file()
    times = [*map( int, lines[ 0 ].split()[1:])]
    distances = [*map( int, lines[ 1 ].split()[1:])]
    result = 1

    for i in range( len( times ) ):
        result *= count_winning_options( times[ i ], distances[ i ] )
    return result


def solve_star2():
    lines = read_file()
    time = int( "".join( lines[ 0 ].split()[1:] ) )
    distance = int("".join( lines[ 1 ].split()[1:]))

    return count_winning_options( time, distance )

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
