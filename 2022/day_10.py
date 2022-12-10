#! /usr/bin/python
import sys, getopt

def solve_star1():
    x=1
    cycle = 0
    time_to_complete = 0
    instruction = 0
    instructions = read_file()
    x_completed = x
    result = 0
    while instruction < len(instructions) or time_to_complete:
        cycle += 1
        if time_to_complete == 0:
            x = x_completed
            if instructions[instruction] == "noop":
                time_to_complete = 1
                x_completed = x
            else:
                time_to_complete = 2
                x_completed = x + int(instructions[instruction].split()[-1])
            instruction += 1
        time_to_complete -= 1
        if cycle % 40 == 20:
            result += cycle * x
    x = x_completed
    return result


def solve_star2():
    x=1
    cycle = 0
    time_to_complete = 0
    instruction = 0
    instructions = read_file()
    x_completed = x
    screen = [[" " for _ in range(40)] for _ in range(6)]
    while instruction < len(instructions) or time_to_complete:
        cycle += 1
        if time_to_complete == 0:
            x = x_completed
            if instructions[instruction] == "noop":
                time_to_complete = 1
                x_completed = x
            else:
                time_to_complete = 2
                x_completed = x + int(instructions[instruction].split()[-1])
            instruction += 1
        time_to_complete -= 1
        if abs((cycle-1) % 40 - x) < 2:
            screen[(cycle-1) // 40][(cycle-1)%40] = "#"
    x = x_completed
    return '\n'.join( ["".join(line) for line in screen])


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
