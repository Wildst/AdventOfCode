#! /usr/bin/python
import sys, getopt

def check_sum(l, n):
    for i, m in enumerate(l):
        if n - m in l[i:]:
            return True
    return False

def solve_star1(preamble_size):
    numbers = [int(n) for n in read_file()]
    for i in range(preamble_size, len(numbers)):
        if not check_sum(numbers[i-preamble_size:i],numbers[i]):
            print(numbers[i])

def solve_star2(preamble_size):
    numbers = [int(n) for n in read_file()]
    for i in range(preamble_size, len(numbers)):
        if not check_sum(numbers[i-preamble_size:i],numbers[i]):
            invalid = numbers[i]

    for i in range(len(numbers)):
        l = 2
        while i+l < len(numbers) and sum(numbers[i:i+l]) < invalid:
            l += 1
        if sum(numbers[i:i+l]) == invalid:
            print(min(numbers[i:i+l]) + max(numbers[i:i+l]))



def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][2:-2] + "in"
    file_dir = "input_files"
    star = 1
    preamble_size = 25
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
            preamble_size = 5

    if star == 1:
        solve_star1(preamble_size)
    elif star == 2:
        solve_star2(preamble_size)









