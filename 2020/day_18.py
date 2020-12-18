#! /usr/bin/python
import sys, getopt

ADD = 1
MULT = 2


def solve_expression(expression):
    sol = 0
    parentheses_count = 0
    action = ADD

    sub_expression = ""

    for c in expression:
        if c == "+":
            if parentheses_count == 0:
                if sub_expression.strip():
                    if action == ADD:
                        sol += int(sub_expression)
                    else:
                        sol *= int(sub_expression)
                    sub_expression = ""
                action = ADD
            else:
                sub_expression += c
        elif c == "*":
            if parentheses_count == 0:
                if sub_expression.strip():
                    if action == ADD:
                        sol += int(sub_expression)
                    else:
                        sol *= int(sub_expression)
                    sub_expression = ""
                action = MULT
            else:
                sub_expression += c
        elif c == "(":
            if parentheses_count != 0:
                sub_expression += c
            parentheses_count += 1
        elif c == ")":
            parentheses_count -= 1
            if parentheses_count == 0:
                if action == ADD:
                    sol += solve_expression(sub_expression)
                else:
                    sol *= solve_expression(sub_expression)
                sub_expression = ""
            else:
                sub_expression += c
        else:
            sub_expression += c

    if sub_expression.strip():
        if action == ADD:
            sol += int(sub_expression)
        else:
            sol *= int(sub_expression)
    return sol

def place_parentheses(expression):
    return '(' + expression.replace("(", "((").replace(")", "))"). replace("*", ")*(") + ')'

def solve_star1():
    print(sum(solve_expression(e) for e in read_file()))
def solve_star2():
    #print(*[solve_expression(place_parentheses(e)) for e in read_file()])
    print(sum(solve_expression(place_parentheses(e)) for e in read_file()))


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









