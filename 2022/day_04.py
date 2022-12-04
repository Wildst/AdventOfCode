#! /usr/bin/python
import sys, getopt

def to_sections( line ):
    a, b = line.split(",")
    a = [*map( int, a.split('-') )]
    b = [*map( int, b.split('-') )]
    return [*range(a[0], a[1]+1)],[*range(b[0],b[1]+1)]

def fully_overlap( section_a, section_b ):
    a = set( section_a )
    b = set( section_b )
    return a.issubset(b) or b.issubset(a)

def overlap(section_a, section_b):
    a = set( section_a )
    b = set( section_b )
    return a.intersection(b)


def solve_star1():
    return len([ 1 for line in read_file() if fully_overlap(*to_sections(line))])

def solve_star2():
    return len([ 1 for line in read_file() if overlap(*to_sections(line))])


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
