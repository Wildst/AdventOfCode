#! /usr/bin/python
import sys, getopt

def solve_star1():
    for line in read_file():
        numbers = [int(n) for n in line.split(",")]
        i = len(numbers) - 1
        recency = {n: i for i, n in enumerate(numbers[:-1])}
        current = numbers[-1]
        stack = [i for i in numbers]
        while i < 2019:
            if current not in recency:
                new = 0
                recency[current] = i
                current = new
            else:
                new = i- recency[current]
                recency[current] = i
                current = new
            i += 1
        print(current)
def solve_star2():
    for line in read_file():
        numbers = [int(n) for n in line.split(",")]
        i = len(numbers) - 1
        recency = {n: i for i, n in enumerate(numbers[:-1])}
        current = numbers[-1]
        stack = [i for i in numbers]
        while i < 30000000-1:
            if current not in recency:
                new = 0
                recency[current] = i
                current = new
            else:
                new = i- recency[current]
                recency[current] = i
                current = new
            i += 1
        print(current)


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









