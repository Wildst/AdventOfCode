#! /usr/bin/python
import sys, getopt

def stringify(chars):
    chars = chars[1:-1]
    result = ""
    while chars:
        if chars.startswith("\\x"):
            result += chr(int(chars[2:4], 16))
            chars = chars[4:]
        elif chars.startswith("\\"):
            result += chars[1]
            chars = chars[2:]
        else:
            result += chars[0]
            chars = chars[1:]
    return result

def encode(chars):
    result = ""
    for char in chars:
        if char == "\"":
            result += "\\\""
        elif char == "\\":
            result += "\\\\"
        else:
            result += char
    return "\"" + result +"\""

def solve_star1():
    result = 0
    for line in read_file():
        result += len(line) - len(stringify(line))
    return result


def solve_star2():
    result = 0
    for line in read_file():
        result += len(encode(line)) - len(line)
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
