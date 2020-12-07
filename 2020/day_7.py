#! /usr/bin/python
import sys, getopt

class Bag:
    def __init__(self, information):
        self.type, contents = information.split(" bags contain ")
        self.contents = {}
        if contents != "no other bags.":
            for bag_type in contents.split(", "):
                amount, *looks, _ = bag_type.split(" ")
                self.contents[" ".join(looks)] = int(amount)

    def __repr__(self):
        line = self.type + " bags contain "
        if len(self.contents) == 0:
            line += "no other bags"
        else:
            for bag in self.contents:
                line += str(self.contents[bag]) + " " + bag
                line += " bags" if self.contents[bag] > 1 else " bag"
                line += ", "
            line = line[:-2]
        return line + "."

    def contains(self, bag_type, bags):
        if self.type == bag_type:
            return False
        for bag in self.contents:
            if bag == bag_type or bags[bag].contains(bag_type, bags):
                return True
        return False

    def get_weight(self, bags):
        s = 0
        if not self.contents:
            return s
        for bag in self.contents:
            s += (1 + bags[bag].get_weight(bags)) * self.contents[bag]
        return s


def solve_star1():
    bags = {bag.type: bag for bag in [Bag(line) for line in read_file()]}
    print(len([bag for bag in bags if bags[bag].contains("shiny gold", bags)]))


def solve_star2():
    bags = {bag.type: bag for bag in [Bag(line) for line in read_file()]}
    print(bags["shiny gold"].get_weight(bags))


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









