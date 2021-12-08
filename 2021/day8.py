#! /usr/bin/python3.8
import sys, getopt

def solve_star1():
    counts = [0]*8
    for line in read_file():
        signal, output = line.split(' | ')
        for i in map(len, output.split()):
            counts[i] += 1
    return counts[2] + counts[3] + counts[4] + counts[7]

def to_bitvec(s):
    v = 0
    for c in s:
        v += 2**'abcdefg'.index(c)
    return v


def decode(signals, output):
    solutions = {}
    bitvecs = [0]*10
    fives = []
    sixes = []
    for signal in signals:
        vec = to_bitvec(signal)
        if len(signal) == 2:
            solutions[vec] = '1'
            bitvecs[1] = vec
        elif len(signal) == 3:
            solutions[vec] = '7'
            bitvecs[7] = vec
        elif len(signal) == 4:
            solutions[vec] = '4'
            bitvecs[4] = vec
        elif len(signal) == 5:
            fives.append(vec)
        elif len(signal) == 6:
            sixes.append(vec)
        elif len(signal) == 7:
            solutions[vec] = '8'
            bitvecs[8] = vec

    # get 3 from 1
    bitvecs[3] = [i for i in fives if bin(i & bitvecs[1]).count('1') == 2][0]
    fives.remove(bitvecs[3])
    solutions[bitvecs[3]] = '3'

    # get 6 from 1
    bitvecs[6] = [i for i in sixes if bin(i & bitvecs[1]).count('1') == 1][0]
    sixes.remove(bitvecs[6])
    solutions[bitvecs[6]] = '6'

    # get 9 from 3
    bitvecs[9] = [i for i in sixes if bin(i & bitvecs[3]).count('1') == 5][0]
    sixes.remove(bitvecs[9])
    solutions[bitvecs[9]] = '9'

    # get 0 from elimination
    bitvecs[0] = sixes[0]
    solutions[bitvecs[0]] = '0'

    # get 5 from 9
    bitvecs[5] = [i for i in fives if bin(i & bitvecs[9]).count('1') == 5][0]
    fives.remove(bitvecs[5])
    solutions[bitvecs[5]] = '5'

    # get 2 from elimination
    bitvecs[2] = fives[0]
    solutions[bitvecs[2]] = '2'
    return int(''.join(solutions[to_bitvec(o)] for o in output ))


def solve_star2():
    #return [*map(lambda l: [*map(lambda p:p.split(), l.split(' | '))],read_file())]
    return sum(map(lambda l: decode(*[*map(lambda p:p.split(), l.split(' | '))]),read_file()))


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
