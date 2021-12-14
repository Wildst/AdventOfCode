#! /usr/bin/python3.8
import sys, getopt

def solve_star1():
    polymer, _, *rules = read_file()
    mapping = {}
    for rule in rules:
        l, r = rule.split(' -> ')
        mapping[l] = r

    for _ in range(10):
        new_polymer = polymer[0]
        for c in polymer[1:]:
            new_polymer += mapping[new_polymer[-1] + c] +c
        polymer = new_polymer

    counts = {}
    for element in set(polymer):
        counts[element] = 0
    for element in polymer:
        counts[element] += 1
    return max(counts.values()) - min(counts.values())

def solve_star2():
    polymer, _, *rules = read_file()
    mapping = {}
    pairs = {}
    additions = {}
    fst = polymer[0]
    last = polymer[-1]
    for rule in rules:
        l, r = rule.split(' -> ')
        mapping[l] = r
        pairs[l] = 0
        additions[l] = [l[0]+r, r+l[1]]

    for i in range(len(polymer)-1):
        pairs[polymer[i:i+2]] += 1


    for i in range(40):
        new_pairs = {}
        for k in pairs:
            for option in additions[k]:
                if option not in new_pairs:
                    new_pairs[option] = pairs[k]
                else:
                    new_pairs[option] += pairs[k]
        pairs = new_pairs

    counts = {}
    for pair in pairs:
        if pair[0] not in counts:
            counts[pair[0]] = pairs[pair]
        else:
            counts[pair[0]]+= pairs[pair]
        if pair[1] not in counts:
            counts[pair[1]] = pairs[pair]
        else:
            counts[pair[1]]+= pairs[pair]
    counts[fst] += 1
    counts[last] += 1
    for element in counts:
        counts[element] //= 2
    return max(counts.values()) - min(counts.values())


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
