#! /usr/bin/python
import sys, getopt

def parse_rules(lines):
    rules = {}
    for rule in lines:
        name, restrictions = rule.split(": ")
        value1, value2 = restrictions.split(" or ")
        lower1, upper1, lower2, upper2 = [int(i) for i in (*value1.split("-"), *value2.split("-"))]

        possibilities = set(range(lower1, upper1 + 1)) | set(range(lower2, upper2 + 1))
        rules[name] = possibilities
    return rules

def solve_star1():
    lines = read_file()
    i = 0
    while lines[i]:
        i += 1
    valid_values = set()
    for v in parse_rules(lines[:i]).values():
        valid_values |= v
    i += 5
    error_rate = 0
    for line in lines[i:]:
        error_rate += sum([int(v) for v in line.split(",") if int(v) not in valid_values])
    print(error_rate)

def solve_star2():
    lines = read_file()
    i = 0
    while lines[i]:
        i += 1
    rules = parse_rules(lines[:i])
    valid_values = set()
    for v in parse_rules(lines[:i]).values():
        valid_values |= v

    i += 2
    our_ticket = [int(v) for v in lines[i].split(",")]
    possible_positions = {name: set(range(len(our_ticket))) for name in rules.keys()}

    for pos, value in enumerate(our_ticket):
        for rule in rules:
            if value not in rules[rule]:
                if pos in possible_positions[rule]:
                    possible_positions[rule].remove(pos)
    for line in lines[i+3:]:
        values = [int(v) for v in line.split(',')]
        if len([v for v in values if v not in valid_values]) == 0:
            for pos, value in enumerate(values):
                for rule in rules:
                    if value not in rules[rule]:
                        if pos in possible_positions[rule]:
                            possible_positions[rule].remove(pos)

    real_positions = [-1 for _ in our_ticket]
    while -1 in real_positions:
        # check if a column can only be one rule
        for i in range(len(our_ticket)):
            if real_positions[i] == -1:
                options = set()
                for rule, positions in possible_positions.items():
                    if i in positions:
                        options.add(rule)
                if len(options) == 1:
                    rule = options.pop()
                    real_positions[i] = rule
                    possible_positions.pop(rule)
        # check if a rule can only be one column
        topop = set()
        for rule, positions in possible_positions.items():
            if len(positions) == 1:
                real_positions[positions.pop()] = rule
                topop.add(rule)
        for rule in topop:
            possible_positions.pop(rule)

    solution = 1
    for i, rule in enumerate(real_positions):
        if rule.startswith("departure"):
            solution *= our_ticket[i]
    print(solution)


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][2:-2] + "in"
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
        solve_star1()
    elif star == 2:
        solve_star2()









