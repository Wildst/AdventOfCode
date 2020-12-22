#! /usr/bin/python
import sys, getopt
from functools import reduce

def solve_star1():
    p1 = []
    p2 = []
    current_player = p1
    for line in read_file():
        if line.startswith("Player"):
            pass
        elif line:
            current_player.append(int(line))
        else:
            current_player = p2
    while p1 and p2:
        card_p1, *p1 = p1
        card_p2, *p2 = p2
        if card_p1 > card_p2:
            p1.append(card_p1)
            p1.append(card_p2)
        else:
            p2.append(card_p2)
            p2.append(card_p1)
        print(*p1)

    if p2:
        p1 = p2
    if p1:
        print(sum([card*value for card, value in zip(p1, range(len(p1), 0, -1))]))
        print('p1', " + ".join([(str(card) + " * " + str(value)) for card, value in zip(p1, range(len(p1), 0, -1))]))
    else:
        print(sum([card*value for card, value in zip(p2, range(len(p2), 0, -1))]))
def solve_star2():
    print(read_file())


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









