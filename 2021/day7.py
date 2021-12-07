#! /usr/bin/python3.8
import sys, getopt

def solve_star1():
    positions = [int(i) for i in read_file()[0].split(',')]
    return min([sum([abs(j-i) for j in positions]) for i in range(max(positions))])
def solve_star2():
    positions = [int(i) for i in read_file()[0].split(',')]
    return min([sum([abs(j-i)*(abs(j-i)+1)//2 for j in positions]) for i in range(max(positions))])


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
