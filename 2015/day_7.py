#! /usr/bin/python
import sys, getopt

def calculate(key, calculations, requirements, memory):
    if key in requirements:
        for requirement in requirements[key]:
            if requirement in calculations:
                memory, calculations = calculate(requirement, calculations, requirements, memory)

    parts = calculations[key].split()
    del calculations[key]
    if len(parts) == 3:
        value = int(parts[0]) if parts[0].isnumeric() else memory[parts[0]]
        memory[parts[-1]] = value
    elif len(parts) == 4:
        value = int(parts[1]) if parts[1].isnumeric() else memory[parts[1]]
        memory[parts[-1]] = ~value % 65536
    else:
        v1 = int(parts[0]) if parts[0].isnumeric() else memory[parts[0]]
        v2 = int(parts[2]) if parts[2].isnumeric() else memory[parts[2]]
        if parts[1] == "AND":
            memory[parts[-1]] = v1 & v2 % 65536
        elif parts[1] == "OR":
            memory[parts[-1]] = v1 | v2 % 65536
        elif parts[1] == "LSHIFT":
            memory[parts[-1]] = v1 << v2 % 65536
        elif parts[1] == "RSHIFT":
            memory[parts[-1]] = v1 >> v2 % 65536
    return memory, calculations


def solve_star1():
    requirements = {}
    calculations = {}
    memory = {}
    for line in read_file():
        parts = line.split()
        if not parts[-1] in requirements:
            requirements[parts[-1]] = []
        if len(parts) == 3:
            if not parts[0].isnumeric():
                requirements[parts[-1]].append(parts[0])
        elif len(parts) == 4:
            if not parts[1].isnumeric():
                requirements[parts[-1]].append(parts[1])
        elif len(parts) == 5:
            if not parts[0].isnumeric():
                requirements[parts[-1]].append(parts[0])
            if not parts[2].isnumeric():
                requirements[parts[-1]].append(parts[2])
        calculations[parts[-1]] = line

    memory, _ = calculate('a', calculations, requirements, memory)
    return memory["a"]

def solve_star2():
    requirements = {}
    calculations = {}
    memory = {}
    for line in read_file():
        parts = line.split()
        if not parts[-1] in requirements:
            requirements[parts[-1]] = []
        if len(parts) == 3:
            if not parts[0].isnumeric():
                requirements[parts[-1]].append(parts[0])
        elif len(parts) == 4:
            if not parts[1].isnumeric():
                requirements[parts[-1]].append(parts[1])
        elif len(parts) == 5:
            if not parts[0].isnumeric():
                requirements[parts[-1]].append(parts[0])
            if not parts[2].isnumeric():
                requirements[parts[-1]].append(parts[2])
        calculations[parts[-1]] = line
    memory, _ = calculate('a', calculations.copy(), requirements, memory)
    memory["b"] = memory["a"]
    del calculations["b"]
    memory, _ = calculate('a', calculations.copy(), requirements, memory)
    return memory["a"]


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
