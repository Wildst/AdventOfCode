#! /usr/bin/python3.8
import sys, getopt

def find_first_bad(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            if not 0 < ord(c) - ord(stack.pop()) <= 2:
                return c
    return None

penalties = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def solve_star1():
    value = 0
    for line in read_file():
        if find_first_bad(line):
            value += penalties[find_first_bad(line)]
    return value


def get_value(stack):
    value = 0
    for element in reversed(stack):
        value *= 5
        value += 1+'([{<'.index(element)
    return value

def find_missing(line):
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            if not 0 < ord(c) - ord(stack.pop()) <= 2:
                return 0
    return get_value(stack)


def solve_star2():
    values = []
    for line in read_file():
        missing = find_missing(line)
        if missing:
            values.append(missing)
    return sorted(values)[len(values)//2]


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
