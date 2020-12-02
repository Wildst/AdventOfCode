#! /usr/bin/python
import sys, getopt

def is_valid_old(line):
    policy, password = line.split(':')
    limits, character = policy.split(" ")
    lower, upper = [int(n) for n in limits.split("-")]
    return lower <= password.count(character) <=upper

def solve_star1():
    print(len([line for line in read_file() if is_valid_old(line)]))

def is_valid_new(line):
    policy, password = line.split(':')
    limits, character = policy.split(" ")
    first, second = [int(n) for n in limits.split("-")]

    valid = False
    valid ^= character == password[first]
    valid ^= character == password[second]
    return valid


def solve_star2():
    print(len([line for line in read_file() if is_valid_new(line)]))

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









