#! /usr/bin/python
import sys, getopt

def solve_star1():
    return sum([calculate_surface(line) for line in read_file()])
def solve_star2():
    return read_file()

def calculate_surface(line):
    l,w,h = map(int, line.split('x'))
    return 2*(l*w+w*h+h*l)+min(l*w,w*h,h*l)

def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][:-2] + "in"
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









