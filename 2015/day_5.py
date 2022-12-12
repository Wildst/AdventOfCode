#! /usr/bin/python
import sys, getopt

def contains_double(word):
    for i, c in enumerate(word[1:]):
        if word[i] == c:
            return True
    return False

def contains_split_pair(word):
    for i, c in enumerate(word[2:]):
        if word[i] == c:
            return True
    return False

def contains_double_pair(word):
    for i in range(len(word) - 2):
        if word[i:i+2] in word[i+2:]:
            return True
    return False

def is_nice(word):
    return word.count("a")+word.count("e")+word.count("i")+word.count("o")+word.count("u") >= 3 and "ab" not in word and "cd" not in word and "pq" not in word and "xy" not in word and contains_double(word)

def is_nice_2(word):
    return contains_double_pair(word) and contains_split_pair(word)

def solve_star1():
    return len([word for word in read_file() if is_nice(word)])
def solve_star2():
    return len([word for word in read_file() if is_nice_2(word)])


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
