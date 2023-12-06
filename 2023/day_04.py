#! /usr/bin/python
import sys, getopt
from functools import lru_cache


def to_number_set( line_part ):
    result = set()
    for part in line_part.split():
        result.add( int( part ) )
    return result

def solve_star1():
    total = 0
    for line in read_file():
        numbers = line.split(":")[1]
        winning, all = map( to_number_set, numbers.split( " | ") )
        amount = len( winning.intersection( all ) )
        if amount > 0:
            total += 1 << amount -1
    return total

@lru_cache
def get_winning_numbers( card ):
    numbers = card.split(":")[1]
    winning, all = map( to_number_set, numbers.split( " | ") )
    return len( winning.intersection( all ) )

def solve_star2():
    cards = read_file()
    pos = 0
    processing = [ i for i in range( len(cards) ) ]
    while pos < len( processing ):
        card = processing[ pos ]
        for i in range( get_winning_numbers( cards[ card ] ) ):
            processing.append( card + i + 1 )
        pos += 1

    return pos

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
