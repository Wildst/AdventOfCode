#! /usr/bin/python
import sys, getopt

def get_instruction( line ):
    if not line.startswith("mul("):
        return ""
    sep = line.find( "," )
    end = line.find( ")" )
    if sep > 7 or sep < 0 or end > sep + 4 or end < sep:
        return ""
    if not line[ 4:sep ].isnumeric() or not line[ sep+1:end].isnumeric():
        return ""
    return line[:end+1]

def do_instruction( line ):
    sep = line.find( "," )
    return int( line[4:sep] ) * int( line[sep+1:-1] )

def get_all_instructions(data):
    instructions = []
    for line in data:
        while line:
            instruction = get_instruction( line )
            if instruction:
                instructions.append( instruction )
            line = line[1:]
    return instructions

def solve_star1():
    instructions = get_all_instructions(read_file())
    return sum( map(do_instruction, instructions))

def get_conditional_instructions( data ):
    instructions = []
    enabled = True
    for line in data:
        while line:
            if enabled:
                instruction = get_instruction( line )
                if instruction:
                    instructions.append( instruction )
                if line.startswith("don't()"):
                    enabled = False
            else:
                enabled = line.startswith("do()")
            line = line[1:]
    return instructions

def solve_star2():
    instructions = get_conditional_instructions(read_file())
    return sum( map(do_instruction, instructions))


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
