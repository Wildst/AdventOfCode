#! /usr/bin/python3.8
import sys, getopt
from itertools import chain

class Board():
    def __init__(self, rows):
        self.rows = [[int(i) for i in row.split()] for row in rows]
        self.marked = [[0 for _ in range(5)] for _ in range(5)]

    def mark(self, number):
        for pos, row in enumerate(self.rows):
            if number in row:
                self.marked[pos][row.index(number)] = 1
        if self.has_won():
            return True
        return False

    def has_won(self):
        return 5 in map(sum, self.marked) or 5 in map(sum, zip(*self.marked))

    def sum_unmarked(self):
        numbers = [*chain.from_iterable(self.rows)]
        modifiers = [*chain.from_iterable(self.marked)]
        return sum(map(lambda a : a[0]*(1-a[1]), zip(numbers,modifiers)))

    def __repr__(self) -> str:
        return '\n'.join(' '.join(f'{str(number):{" "}{">"}{2}}' for number in row) for row in self.rows) + '\n'

    def print_markers(self):
        print('\n'.join(' '.join('#' if number else '_' for number in row) for row in self.marked) + '\n')

def solve_star1():
    lines = read_file()
    numbers = [int(i) for i in lines[0].split(',')]
    boards = []
    for i in range(2, len(lines), 6):
        boards.append(Board(lines[i:i+5]))
    for number in numbers:
        for board in boards:
            if board.mark(number):
                return board.sum_unmarked()* number

def solve_star2():
    lines = read_file()
    numbers = [int(i) for i in lines[0].split(',')]
    boards = []
    for i in range(2, len(lines), 6):
        boards.append(Board(lines[i:i+5]))
    pos = 0
    while len(boards) > 1:
        boards = [board for board in boards if not board.mark(numbers[pos])]
        pos += 1
    board = boards[0]
    while not board.mark(numbers[pos]):
        pos += 1
    return boards[0].sum_unmarked()*numbers[pos]


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









