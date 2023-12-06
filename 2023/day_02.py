#! /usr/bin/python
import sys, getopt

colors = ["red", "green", "blue"]

def get_empty_set():
    return {
        "red": 0,
        "green": 0,
        "blue": 0
    }

def parse_line( line ):
    parts = line.split(':')
    id = int( parts[ 0 ][5:] )
    sets = parts[ 1 ].split( ";" )
    result = []
    for set in sets:
        parsed_set = get_empty_set()
        for group in set.split(","):
            amount, color = group.split()
            parsed_set[ color ] = int( amount )
        result.append( parsed_set )

    return id, result

def is_possible( amounts, game ):
    for set in game:
        for color in colors:
            if amounts[ color ] < set[ color ]:
                return False
    return True

def minimal_amounts( game ):
    amounts = get_empty_set()
    for set in game:
        for color in colors:
            amounts[ color ] = max( amounts[ color ], set[ color ] )
    return amounts

def solve_star1():
    result = 0
    amounts = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    games = [ parse_line( line ) for line in read_file() ]
    for game in games:
        id, sets = game
        if is_possible( amounts, sets ):
            result += id
    return result


def solve_star2():
    result = 0
    games = [ parse_line( line ) for line in read_file() ]
    for game in games:
        id, sets = game
        amounts = minimal_amounts( sets )
        result += amounts[ "red" ] * amounts[ "green" ] * amounts[ "blue" ]
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
