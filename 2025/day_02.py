#! /usr/bin/python
import sys, getopt

def is_invalid(id):
    s = str(id)
    return s[len(s)//2:] == s[:len(s)//2]

def is_repetition(id):
    s = str(id)
    for repetition_size in range(1,len(s)//2+1):
        if s == s[:repetition_size] * (len(s) //repetition_size):
            return True
    return False

def find_invalid(start,end, filter=is_invalid):
    s = int(start)
    e = int(end)
    return [id for id in range(s, e+1) if filter(id)]

def solve_star1():
    result = 0
    for line in read_file():
        for range in line.split(","):
            if not range:
                continue
            a = find_invalid(*range.split("-"))
            result += sum(find_invalid(*range.split("-")))

    return result
def solve_star2():
    result = 0
    for line in read_file():
        for range in line.split(","):
            if not range:
                continue
            a = find_invalid(*range.split("-"))
            result += sum(find_invalid(*range.split("-"), is_repetition))

    return result


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
