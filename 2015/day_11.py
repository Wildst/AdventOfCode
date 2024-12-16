#! /usr/bin/python
import sys, getopt

def increment(password):
    if password[-1] == "z":
        if len( password ) == 5:
            print( increment( password[:-1] ) )
        return increment(password[:-1]) +"a"
    else:
        return password[:-1] + chr(ord(password[-1])+1)

def has_increasing_straight(password, length=3):
    for i in range(len(password) - length):
        value = ord(password[i])
        amount = 1
        for j in range(length-1):
            if ord(password[i+j+1]) == value + j + 1:
                amount += 1
        if amount >= length:
            return True
    return False

def has_good_chars(password, bad_chars="iol"):
    for bad_char in bad_chars:
        if bad_char in password:
            return False
    return True

def has_pairs(password, amount=2):
    pairs = 0
    prev = ""
    for c in password:
        if prev == c:
            prev = ""
            pairs += 1
        else:
            prev = c
    return pairs >= amount

def is_good_1(password):
    return has_increasing_straight(password) and has_good_chars(password) and has_pairs(password)

def solve_star1():
    password = read_file()[0]
    password = increment( password )
    while not is_good_1(password):
        password = increment(password)
    return password

def solve_star2():
    password = read_file()[0]
    password = increment( password )
    while not is_good_1(password):
        password = increment(password)
    password = increment( password )
    while not is_good_1(password):
        password = increment(password)
    return password


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
