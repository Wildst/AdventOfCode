#! /usr/bin/python
import sys, getopt

def solve_star1():
    memory = {}
    mask = (0, 0)
    for line in read_file():
        command, value = line.split(" = ")
        if command == "mask":
            mask = (int(value.replace("X", "0"), 2), int(value.replace("X", "1"), 2))
        else:
            location = int(command[4:-1])
            memory[location] = (int(value) | mask[0]) & mask[1]
    print(sum(memory[value] for value in memory))

def get_floating_options(indices, start_value):
    if not indices:
        return [start_value]

    return [*get_floating_options(indices[1:], start_value),
            *get_floating_options(indices[1:], start_value ^ 2 ** indices[0])]

def solve_star2():
    memory = {}
    mask = ""
    m = 0
    for line in read_file():
        command, value = line.split(" = ")
        if command == "mask":
            mask = value
        else:
            location = int(command[4:-1])
            value = int(value)
            floating = []
            for i, c in enumerate(reversed(mask)):
                if c == "1":
                    location |= 2**i
                elif c == "X":
                    floating.append(i)
            for position in get_floating_options(floating, location):
                memory[position] = value
    print(sum(memory[value] for value in memory))


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









