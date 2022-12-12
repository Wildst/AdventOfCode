#! /usr/bin/python
import sys, getopt
import hashlib

def solve_star1():
    i = 0
    while not hashlib.md5((read_file()[0] + str(i)).encode()).hexdigest().startswith('00000'):
        i += 1
    return i


def solve_star2():
    i = 0
    while not hashlib.md5((read_file()[0] + str(i)).encode()).hexdigest().startswith('000000'):
        i += 1
    return i


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
