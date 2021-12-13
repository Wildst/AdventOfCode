#! /usr/bin/python3.8
import sys, getopt

def fold(dots, n, fold_x=True):
    folded = set()
    for x,y in dots:
        if fold_x:
            folded.add((x if x <= n else n-(x-n), y))
        else:
            folded.add((x, y if y <= n else n-(y-n)))
    return folded

def print_dots(dots):
    max_x, max_y = 0,0
    for x,y in dots:
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    m = [[' ' for x in range(max_x+1)] for y in range(max_y+1)]
    for x,y in dots:
        m[y][x] = '#'
    for line in m:
        print(''.join(line))

def solve_star1():
    lines = read_file()
    i = lines.index('')
    dots, folds = [*map(lambda l: tuple(map(int, l.split(','))), lines[:i])], lines[i+1:]
    return len(fold(dots, int(folds[0].split('=')[1]), 'x' in folds[0]))

def solve_star2():
    lines = read_file()
    i = lines.index('')
    dots, folds = [*map(lambda l: tuple(map(int, l.split(','))), lines[:i])], lines[i+1:]
    for command in folds:
        dots = fold(dots, int(command.split('=')[1]), 'x' in command)
    print_dots(dots)
    return None


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
