#! /usr/bin/python
import sys, getopt

class Instruction:
    def __init__(self, line):
        self.operation, amount = line.split(" ")
        self.amount = int(amount)

    def __repr__(self):
        return self.operation + " " + str(self.amount)


def solve_star1():
    instructions = [Instruction(line) for line in read_file()]
    ip = 0
    passed = set()
    acc = 0
    while ip not in passed:
        passed.add(ip)
        if instructions[ip].operation == "nop":
            ip += 1
        elif instructions[ip].operation == "acc":
            acc += instructions[ip].amount
            ip += 1
        elif instructions[ip].operation == "jmp":
            ip += instructions[ip].amount

    print(acc)

def solve_star2():
    instructions = [Instruction(line) for line in read_file()]
    ip = 0
    passed = set()
    acc = 0

    changed_something = False
    changed_pointer, changed_acc = 0, 0
    backup_set = set()

    while ip < len(instructions):
        if ip in passed:
            passed = backup_set
            ip = changed_pointer
            acc = changed_acc
            changed_something = False
        passed.add(ip)
        if instructions[ip].operation == "nop":
            if changed_something:
                ip += 1
            else:
                backup_set = set(passed)
                changed_acc = acc
                changed_pointer = ip + 1

                ip += instructions[ip].amount
                changed_something = True

        elif instructions[ip].operation == "acc":
            acc += instructions[ip].amount
            ip += 1
        elif instructions[ip].operation == "jmp":
            if changed_something:
                ip += instructions[ip].amount
            else:
                backup_set = set(passed)
                changed_acc = acc
                changed_pointer = ip + instructions[ip].amount

                ip += 1
                changed_something = True
    print(acc)


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









