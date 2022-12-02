#! /usr/bin/python
import sys, getopt

rock = 1
paper = 2
scissors = 3

def to_item( char ):
    return {"A": rock, "B": paper, "C": scissors, "X":rock, "Y":paper, "Z":scissors }[ char ]

def play( opponent, player ):
    if opponent == player:
        return 3 # Draw
    if player == 1 + opponent % 3:
        return 6
    return 0 # loss

def find_play( opponent, result ):
    pick = 1
    while play( opponent, pick ) != result:
        pick += 1
    return pick

def solve_star1():
    score = 0
    for opponent, player in [ map( to_item, line.split() ) for line in read_file() ]:
        score += player + play( opponent, player )
        print( opponent, player, play( opponent, player ) )
    return score

def solve_star2():
    score = 0
    for opponent, result in [ map( to_item, line.split() ) for line in read_file() ]:
        result = result * 3 - 3
        player = find_play( opponent, result )
        score += player + result
    return score


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
