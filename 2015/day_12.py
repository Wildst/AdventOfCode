#! /usr/bin/python
import sys, getopt
import json


def get_value( data ):
    if type( data ) == int:
        return data
    if type( data ) == str:
        return 0
    if type( data ) == list:
        return sum( get_value( item ) for item in data )
    if type( data ) == dict:
        result = 0
        for key in data:
            result += get_value( key )
            result += get_value( data[ key ] )
        return result
    print( type( data ), data )
    return 0

def get_value_without_red( data ):
    if type( data ) == int:
        return data
    if type( data ) == str:
        return 0
    if type( data ) == list:
        return sum( get_value_without_red( item ) for item in data )
    if type( data ) == dict:
        result = 0
        for key in data:
            if data[ key ] == "red":
                return 0
            result += get_value_without_red( key )
            result += get_value_without_red( data[ key ] )
        return result
    print( type( data ), data )
    return 0


def solve_star1():
    for line in read_file():
        data = json.loads( line )
        return get_value( data )

def solve_star2():
    for line in read_file():
        data = json.loads( line )
        return get_value_without_red( data )


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
