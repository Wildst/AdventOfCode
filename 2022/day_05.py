#! /usr/bin/python
import sys, getopt

def solve_star1():
    pos = 0
    lines = read_file()
    while lines[pos].strip():
        pos += 1
    original_stacks = [*reversed(lines[:pos-1])]
    stacks = [[] for _ in lines[pos-1].split()]
    for crates in original_stacks:
        for i, stack in enumerate(stacks):
            if(len(crates) > 4*i+1 and crates[4*i + 1] != " "):
                stack.append(crates[4*i+1])

    for line in lines[pos+1:]:
        _, amount, _, origin, _, destination = line.split()
        for _ in range(int(amount)):
            stacks[int(destination)-1].append(stacks[int(origin)-1][-1])
            stacks[int(origin)-1].pop()

    return "".join(stack[-1] for stack in stacks)
def solve_star2():
    pos = 0
    lines = read_file()
    while lines[pos].strip():
        pos += 1
    original_stacks = [*reversed(lines[:pos-1])]
    stacks = [[] for _ in lines[pos-1].split()]
    for crates in original_stacks:
        for i, stack in enumerate(stacks):
            if(len(crates) > 4*i+1 and crates[4*i + 1] != " "):
                stack.append(crates[4*i+1])

    for line in lines[pos+1:]:
        _, amount, _, origin, _, destination = line.split()
        amount = int(amount)
        origin = int(origin)-1
        destination = int(destination)-1
        stacks[destination] += stacks[origin][-amount:]
        stacks[origin] = stacks[origin][:-amount]
    return "".join(stack[-1] for stack in stacks)



def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line for line in file]


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
