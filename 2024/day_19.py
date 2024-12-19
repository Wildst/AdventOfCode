#! /usr/bin/python
import sys, getopt
from functools import lru_cache

def parse_input( data ):
    designs = set( data[0].split( ", " ) )
    return designs, data[2:]

def is_possible( request, designs ):
    if not request:
        return True
    for design in designs:
        if request.startswith( design ) and is_possible( request[len(design):], designs ):
            return True
    return False

class ArrangementFactory:
    def __init__( self, designs ):
        self.designs = designs

    @lru_cache
    def count_options( self, request ):
        if not request:
            return 1
        total = 0
        for design in self.designs:
            if request.startswith( design ):
                total += self.count_options( request[len(design):] )
        return total


def solve_star1():
    designs, requests = parse_input( read_file( ) )
    return len( [ request for request in requests if is_possible( request, designs ) ] )


def solve_star2():
    designs, requests = parse_input( read_file( ) )
    factory = ArrangementFactory( designs )
    return sum( [ factory.count_options( request ) for request in requests ] )


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
