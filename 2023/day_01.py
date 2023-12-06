#! /usr/bin/python
import sys, getopt

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_calibration( l ):
    s = 0
    for line in l:
        digits = [ int(c) for c in line if c.isdigit()]
        s += 10 * digits[ 0 ] + digits[ -1 ]
    return s

def read_numbers( line ):
    for number in numbers.keys():
        line = line.replace( number, number+numbers[ number ]+number )
    return line

def solve_star1():
    return get_calibration( read_file() )

def solve_star2():
    return get_calibration([ read_numbers( line ) for line in read_file() ])


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
