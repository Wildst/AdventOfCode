#! /usr/bin/python
import sys, getopt

def solve_star1():
    numbers = [int(n) for n in read_file()]
    for i, n in enumerate(numbers):
        if 2020 -n in numbers[i+1:]:
            print((2020-n) * n)
def solve_star2():
    numbers = [int(n) for n in read_file()]
    for i, n in enumerate(numbers):
        for j, m in enumerate(numbers[i+1:]):
            if 2020 -n-m in numbers[j+1:]:
                print((2020-n-m) * n *m)


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







