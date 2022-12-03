#! /usr/bin/python
import sys, getopt

def split_compartiments(rucksack):
    compartiment_size = len(rucksack)//2
    return rucksack[:compartiment_size], rucksack[compartiment_size:]

def find_common(part1, part2, part3="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    return set(part1).intersection(set(part2)).intersection(set(part3)).pop()

def calculate_priority(item):
    if item.upper() == item:
        return 27 + ord(item) - ord("A")
    else:
        return 1 + ord(item) - ord("a")

def solve_star1():
    return sum(calculate_priority(find_common(*split_compartiments(rucksack))) for rucksack in read_file())

def solve_star2():
    rucksacks = iter(read_file())
    return sum(calculate_priority(find_common(*group)) for group in zip(rucksacks, rucksacks, rucksacks))


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
