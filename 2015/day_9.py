#! /usr/bin/python
import sys, getopt

def find_best(start, destinations, distances):
    best = sum(distances.values())
    if not destinations:
        return 0
    for destination in destinations:
        others = destinations.copy()
        others.remove(destination)
        test = distances[(start, destination)] + find_best(destination, others, distances)
        if test < best:
            best = test
    return best

def find_worst(start, destinations, distances):
    best = 0
    if not destinations:
        return 0
    for destination in destinations:
        others = destinations.copy()
        others.remove(destination)
        test = distances[(start, destination)] + find_worst(destination, others, distances)
        if test > best:
            best = test
    return best

def solve_star1():
    distances = {}
    locations = set()
    for line in read_file():
        start, _, end, _, distance = line.split()
        locations.add(start)
        locations.add(end)
        distances[(start, end)] = int(distance)
        distances[(end, start)] = int(distance)

    best = sum(distances.values())
    for destination in locations:
        others = locations.copy()
        others.remove(destination)
        test = find_best(destination, others, distances)
        if test < best:
            best = test
    return best

def solve_star2():
    distances = {}
    locations = set()
    for line in read_file():
        start, _, end, _, distance = line.split()
        locations.add(start)
        locations.add(end)
        distances[(start, end)] = int(distance)
        distances[(end, start)] = int(distance)

    best = 0
    for destination in locations:
        others = locations.copy()
        others.remove(destination)
        test = find_worst(destination, others, distances)
        if test > best:
            best = test
    return best


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


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
