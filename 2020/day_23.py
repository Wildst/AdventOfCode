#! /usr/bin/python
import sys, getopt



def solve_star1():
    cups = [int(i) for i in read_file()[0]]
    # execute 100 rounds
    for _ in range(100):
        # pick up the cups
        picked_up = cups[1:4]
        cups = cups[:1] + cups[4:]
        value = cups[0]
        # find the destination
        value -= 1
        if value == 0:
            value = 9
        while value not in cups:
            value -= 1
            if value == 0:
                value = 9
        destination = cups.index(value)

        # insert cups again
        cups = cups[:destination + 1] + picked_up + cups[destination + 1:]

        # put next cup in front
        cups = cups[1:] + cups[:1]
    # put the 1 in the front
    while cups[0] != 1:
        cups = cups[1:] + cups[:1]

    print("".join([str(i) for i in cups[1:]]))

"""
    for debugging only
"""
def reassemble(l, start=1):
    reassembled = [start]
    current = start
    while l[current] != start:
        current = l[current]
        reassembled.append(current)
    return reassembled


def solve_star2():
    cups = [i+1 for i in range(1000001)]
    cups[0] = "Nothing here"
    last = -1
    for value in read_file()[0]:
        value = int(value)
        cups[last] = value
        last = value
    cups[last] = 10
    current = cups[-1]
    # execute 10000000 rounds
    for i in range(10000000):
        # pick up the cups
        picked_up = [cups[current]]
        for i in range(2):
            picked_up.append(cups[picked_up[-1]])
        value = current
        # find the destination
        value -= 1
        if value == 0:
            value = 1000000
        while value in picked_up:
            value -= 1
            if value == 0:
                value = 1000000
        cups[value], cups[current], cups[picked_up[-1]] = cups[current], cups[picked_up[-1]], cups[value]

        # put next cup in front
        current = cups[current]
    first_cup = cups[1]
    second_cup = cups[first_cup]
    print(first_cup * second_cup)


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









