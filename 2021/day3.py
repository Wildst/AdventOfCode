#! /usr/bin/python3.8
import sys, getopt

def get_commons(lines):
    counts = [0]*len(lines[1])
    for line in lines:
        for i, b in enumerate(line):
            counts[i] += int(b)
    return ''.join('1' if count >= len(lines)/2 else '0' for count in counts)


def solve_star1():
    commons=get_commons(read_file())
    gamma = int(commons,2)
    return gamma * (gamma ^ (2**len(commons)  - 1))

def solve_star2():
    lines = read_file()

    # find oxygen generator rating
    oxygen=lines
    pos = 0
    while len(oxygen) > 1:
        oxygen=[line for line in oxygen if line[pos]==get_commons(oxygen)[pos]]
        pos += 1

    # find co2 scrubber rating
    co2=lines
    pos = 0
    while len(co2) > 1:
        co2=[line for line in co2 if line[pos]!=get_commons(co2)[pos]]
        pos += 1

    return int(oxygen[0], 2)* int(co2[0],2)



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









