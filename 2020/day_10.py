#! /usr/bin/python
import sys, getopt
from functools import lru_cache

def solve_star1():
    outlets = sorted([int(i) for i in read_file()])
    differences = [0,0,1]
    differences[outlets[0] - 1] += 1
    for i, outlet in enumerate(outlets[:-1]):
        differences[outlets[i+1] - outlet - 1 ] += 1
    print(differences)
    print(differences[0] * differences[2])

@lru_cache
def get_option_count(rowlength):
    if rowlength <= 0:
        return 0
    if rowlength == 1:
        return 1
    # (1, 2, 3, 4)
    return sum([get_option_count(rowlength -i) for i in range(1, 4) ])


def solve_star2():
    outlets = sorted([int(i) for i in read_file()])
    outlets = [0, *outlets, outlets[-1] + 3]

    total = 1
    rowlength = 1

    for i, outlet in enumerate(outlets[:-1]):
        if outlets[i+1] - outlet == 3:
            total *= get_option_count(rowlength)
            rowlength = 1
        elif outlets[i+1] - outlet == 1:
            rowlength += 1

    print(total)




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









