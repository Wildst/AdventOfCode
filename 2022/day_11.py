#! /usr/bin/python
import sys, getopt

class Monkey:
    def __init__(self, lines, relief=3):
        self.items = [*map(int, lines[1].split(":")[-1].strip().split(","))]
        self.operation = lines[2].split("=")[-1].strip()
        self.test = int(lines[3].split()[-1])
        self.destinations = int(lines[4].split()[-1]), int(lines[5].split()[-1])
        self.inspections = 0
        self.relief = relief

    def __str__(self):
        return "Monkey:\n  Current items: %s\n  Operation: new = %s\n  Test: divisible by %i\n    If true: throw to monkey %i\n    If false: throw to monkey %i" % (", ".join(map(str, self.items)), self.operation, self.test, self.destinations[0], self.destinations[1])

    def __repr__(self):
        return str(self)

    def throw(self, monkeys, simplifier=lambda x: x):
        for item in self.items:
            worry_lvl = eval(self.operation.replace("old", str(item)))
            worry_lvl //= self.relief
            monkeys[self.destinations[ 1 if worry_lvl % self.test else 0]].items.append(simplifier(worry_lvl))
            self.inspections += 1
        self.items.clear()

def print_items(monkeys):
    for i, monkey in enumerate(monkeys):
        print("Monkey %i: %s" %(i, ", ".join(map(str, monkey.items))))

def solve_star1():
    lines = []
    monkeys = []
    for line in read_file():
        if line:
            lines.append(line)
        else:
            monkeys.append(Monkey(lines))
            lines = []
    if lines:
        monkeys.append(Monkey(lines))

    for _ in range(20):
        for monkey in monkeys:
            monkey.throw(monkeys)
    activities = sorted(monkey.inspections for monkey in monkeys)

    return activities[-1]*activities[-2]


def solve_star2():
    lines = []
    monkeys = []
    for line in read_file():
        if line:
            lines.append(line)
        else:
            monkeys.append(Monkey(lines, 1))
            lines = []
    if lines:
        monkeys.append(Monkey(lines, 1))

    check = 1
    for monkey in monkeys:
        check *= monkey.test
    for _ in range(10000):
        for monkey in monkeys:
            monkey.throw(monkeys, lambda x: x%check)
    activities = sorted(monkey.inspections for monkey in monkeys)

    return activities[-1]*activities[-2]


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
