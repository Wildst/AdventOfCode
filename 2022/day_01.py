#! /usr/bin/python
import sys, getopt

def solve_star1(): # oneliner
    return max([ sum( map( int, elf.split() ) ) for elf in "\n".join(read_file()).split("\n\n") ])

def solve_star1_clear():
    elves = [0]
    for line in read_file():
        if not line.strip():
            elves.append( 0 )
        else:
            elves[ -1 ] += int( line )
    return max( elves )

def solve_star2():
    return sum( sorted( sum( map( int, elf.split() ) ) for elf in "\n".join(read_file()).split("\n\n") )[-3:])

def solve_star2_clear():
    elves = [0]
    for line in read_file():
        if not line.strip():
            elves.append( 0 )
        else:
            elves[ -1 ] += int( line )
    elves.sort()
    return sum( elves[-3:] )


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][2:-2] + "in"
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
