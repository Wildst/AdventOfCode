#! /usr/bin/python
import sys, getopt

def solve_star1():
    passes = [ int(boarding_pass.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for boarding_pass in read_file()]
    print(max(passes))



def solve_star2():
    passes = sorted([ int(boarding_pass.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for boarding_pass in read_file()])
    for index, seat in enumerate(passes[:-1]):
        if passes[index + 1] == seat + 2:
            print(seat + 1)


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









