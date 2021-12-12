#! /usr/bin/python3.8
import sys, getopt

class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def connect(self, other):
        self.connections.append(other)

    def is_interesting(self, path):
        return self.is_big() or self.name not in path

    def is_big(self):
        return self.name.isupper()

    def __repr__(self):
        return self.name + ": " + ', '.join(self.connections)

def get_caves():
    caves = {}
    for line in read_file():
        a, b = line.split('-')
        if a not in caves:
            caves[a] = Cave(a)
        if b not in caves:
            caves[b] = Cave(b)
        caves[a].connect(b)
        caves[b].connect(a)
    return caves

def find_paths(caves, path):
    paths = []
    for cave in caves[path[-1]].connections:
        cave = caves[cave]
        if cave.is_interesting(path):
            if cave.name == 'end':
                paths.append([*path, cave.name])
            else:
                paths += find_paths(caves, [*path, cave.name])
    return paths

def solve_star1():
    caves = get_caves()
    current_path = ['start']
    return len(find_paths(caves, current_path))

def find_more_paths(caves, path):
    paths = []
    for cave in caves[path[-1]].connections:
        cave = caves[cave]
        if cave.is_interesting(path):
            if cave.name == 'end':
                paths.append([*path, cave.name])
            else:
                paths += find_more_paths(caves, [*path, cave.name])
        elif cave.name != 'start':
            paths += find_paths(caves, [*path, cave.name])
    return paths

def solve_star2():
    caves = get_caves()
    current_path = ['start']
    return len(find_more_paths(caves, current_path))


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
