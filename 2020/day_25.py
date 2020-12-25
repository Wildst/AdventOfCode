#! /usr/bin/python
import sys, getopt

def transform(value=1, subject_number=7, loop_size=1):
    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227

    return value


def solve_star1():
    card_pk, door_pk = [int(i) for i in read_file()]
    # calculate card's loop size
    card = 1
    card_loop_size = 0
    while card != card_pk:
        card = transform(value=card, subject_number=7)
        card_loop_size += 1

    door = 1
    door_loop_size = 0
    while door != door_pk:
        door = transform(door, subject_number=7)
        door_loop_size += 1


    print(transform(subject_number=door_pk, loop_size=card_loop_size), transform(subject_number=card_pk, loop_size=door_loop_size))

def solve_star2():
    pass
    # No second part for the last day :(


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









