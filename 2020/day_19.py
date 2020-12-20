#! /usr/bin/python
import sys, getopt
from itertools import product
from functools import lru_cache


class RuleChecker():
    def __init__(self, rule_number, rule_requirements):
        self.number = rule_number
        self.options = []
        for option in rule_requirements.split(" | "):
            if '"' in option:
                self.options.append(option.strip('"'))
            else:
                self.options.append([int(i) for i in option.split(" ")])
        self.possible_lengths = False

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "'"+ str(self.number) + ": " + " | ".join(['"'+option+'"' if isinstance(option, str) else " ".join(str(i) for i in option) for option in self.options]) + "'"

    def len_restriction(self, all_rules, max_size=-1):
        if not self.possible_lengths:
            self.possible_lengths = set()
            if self.number == 8:
                # abuse that all other rules only have 1 possible length
                rule_42 = min(all_rules[42].len_restriction(all_rules))
                self.possible_lengths= set(range(rule_42, max_size, rule_42))
            elif self.number == 11:
                # abuse that all other rules only have 1 possible length
                rule_42 = min(all_rules[42].len_restriction(all_rules))
                rule_31 = min(all_rules[31].len_restriction(all_rules))
                self.possible_lengths= set(range(rule_42+rule_31, max_size, rule_42+rule_31))

            else:
                for option in self.options:
                    if isinstance(option, str):
                        self.possible_lengths.add(len(option))
                    else:
                        self.possible_lengths |= set([sum(combination) for combination in
                                        product(
                                            *[all_rules[i].len_restriction(all_rules) for i in option])])
        return self.possible_lengths

    def check_option(self, option, message, all_rules):
        if len(option) == 0:
            return len(message) == 0
        if len(message) == 0:
            return False
        else:
            first_rule = all_rules[option[0]]
            for length in first_rule.len_restriction(all_rules):
                if len(message) >= length and first_rule.check_rule(message[:length], all_rules) \
                    and self.check_option(option[1:], message[length:], all_rules):
                    return True
        return False

    def check_rule(self, message, all_rules):
        if len(message) not in self.len_restriction(all_rules):
            return False
        for option in self.options:
            if isinstance(option, str):
                if option == message:
                    return True
            else:
                if self.check_option(option, message, all_rules):
                    return True
        return False


def solve_star1():
    i = 0
    lines = read_file()
    rules = {}
    while lines[i]:
        number, requirements = lines[i].split(": ")
        number = int(number)
        rules[number] = RuleChecker(number, requirements)
        i += 1
    print(len([message for message in lines[i+1:] if rules[0].check_rule(message, rules)]))
def solve_star2():
    i = 0
    lines = read_file()
    rules = {}
    while lines[i]:
        number, requirements = lines[i].split(": ")
        number = int(number)
        rules[number] = RuleChecker(number, requirements)
        i += 1

    rules[8] = RuleChecker(8, "42 | 42 8")
    rules[11] = RuleChecker(11, "42 31 | 42 11 31")

    m = max(*[len(message) for message in lines[i+1:]])

    rules[8].len_restriction(rules, m)
    rules[11].len_restriction(rules, m)
    c = 0
    print(len([message for message in lines[i+1:] if rules[0].check_rule(message, rules)]))


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









