#! /usr/bin/python
import sys, getopt
from functools import lru_cache

def change(stone):
    if stone == 0:
        return [ 1 ]
    if len( str(stone) ) % 2 == 0:
        l = len(str( stone ) ) // 2
        return [ int( str(stone)[ : l] ), int( str(stone)[ l: ] ) ]
    return [ stone * 2024 ]

@lru_cache( 4096 )
def do_blink( stone, times ):
    if times == 0:
        return 1
    result = 0
    for new_stone in change( stone ):
        result += do_blink( new_stone, times - 1 )
    return result

def solve_star1():
    stones = [ int( s ) for s in read_file()[ 0 ].split( )]
    result = 0
    for stone in stones:
        result += do_blink( stone, 25 )
    return result


def solve_star2():
    stones = [ int( s ) for s in read_file()[ 0 ].split( )]
    result = 0
    for stone in stones:
        result += do_blink( stone, 75 )
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
