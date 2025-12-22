#! /usr/bin/python
import sys, getopt
from functools import reduce

def solve(problem):
    operator = problem[-1]
    if operator == "+":
        return reduce(lambda x, y: x + y, map(int,problem[:-1]))
    else:
        return reduce(lambda x, y: x * y, map(int,problem[:-1]))

def solve_full(problem):
    operator = problem[0][-1]
    numbers = [*map(int, [line[:-1] for line in problem])]
    if operator == "+":
        return reduce(lambda x, y: x + y, numbers)
    else:
        return reduce(lambda x, y: x * y, numbers)
def solve_star1():
    return sum( solve(problem) for problem in zip(*[line.split() for line in read_file()]))

def solve_star2():
    lines = read_file()
    longest = max(map(len, lines))
    lines = [ line[:-1] + " "*(longest -len(line)) for line in lines]

    problems = []
    problem = []
    for line in ["".join(c) for c in zip(*lines)]:
        if line.strip():
            problem.append(line)
        else:
            problems.append(problem)
            problem = []
    problems.append(problem)
    return sum(solve_full(problem) for problem in problems)


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line for line in file]


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
