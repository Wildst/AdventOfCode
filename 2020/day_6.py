#! /usr/bin/python
import sys, getopt

def solve_star1():
    s = 0
    group = ""
    for passenger in read_file():
        if not passenger:
            s += len(set(group))
            group = ""
        else:
            group += passenger

    s += len(set(group))
    print(s)


def solve_star2():
    s = 0
    group = set([chr(ord("a") + i) for i in range(26)])
    for passenger in read_file():
        if not passenger:
            s += len(group)
            group = set([chr(ord("a") + i) for i in range(26)])
        else:
            group &= set(passenger)

    s += len(set(group))
    print(s)



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
        solve_star1()
    elif star == 2:
        solve_star2()









