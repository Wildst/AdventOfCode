#! /usr/bin/python
import sys, getopt

def parse_input( data ):
    result = []
    for line in data:
        solution, numbers = line.split(': ')
        result.append( ( int( solution ), [ *map( int, numbers.split() ) ] ) )
    return result

def can_be_true( solution, numbers ):
    if len( numbers ) == 0:
        return False
    if len( numbers ) == 1:
        return solution == numbers[-1]
    # try summation:
    if can_be_true( solution - numbers[-1], numbers[ :-1 ] ):
        return True
    # try multiplication
    if solution % numbers[-1]:
       return False
    return can_be_true( solution // numbers[-1], numbers[ :-1 ] )

def solve_star1():
    equations = parse_input( read_file() )
    return sum([ solution for solution, numbers in equations if can_be_true( solution, numbers ) ])

def can_be_true_2( solution, numbers ):
    if len( numbers ) == 1:
        return solution == numbers[-1]
    # try summation
    if can_be_true_2( solution, [ numbers[0] + numbers[1]] + numbers[ 2: ] ):
        return True
    # try concatenation
    if can_be_true_2( solution, [ int( str( numbers[ 0 ]) + str( numbers[1] ) ) ] + numbers[ 2: ] ):
        return True
    # try multiplication
    return can_be_true_2( solution, [ numbers[ 0 ] * numbers[ 1 ] ] + numbers[ 2: ] )

def solve_star2():
    equations = parse_input( read_file() )
    return sum([ solution for solution, numbers in equations if can_be_true_2( solution, numbers ) ])


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
