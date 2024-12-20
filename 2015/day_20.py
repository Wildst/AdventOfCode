#! /usr/bin/python
import sys, getopt
import math

def solve_star1():
    target = int( read_file()[ 0 ] )
    houses = [ 0 for _ in range( target // 10 ) ]
    for elf in range( 1, len( houses ) ):
        for house in range( elf, len(houses), elf ):
            houses[ house ] += 10*elf
    for house, presents in enumerate( houses ):
        if presents >= target:
            return house
    return houses


def solve_star2():
    target = int( read_file()[ 0 ] )
    houses = [ 0 for _ in range( target // 10 ) ]
    for elf in range( 1, len( houses ) ):
        for house in range( elf, len(houses), elf ):
            if house > 50*elf:
                break
            houses[ house ] += 11*elf
    for house, presents in enumerate( houses ):
        if presents >= target:
            return house
    return houses



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
