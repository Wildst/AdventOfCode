#! /usr/bin/python3.8
import sys, getopt

def split_snail(snailstring):
    counter = 0
    snailstring = snailstring[1:-1]
    for i, c in enumerate(snailstring):
        if c == '[':
            counter += 1
        elif c == ']':
            counter -= 1
        if counter == 0 and c == ',':
            return snailstring[:i], snailstring[i+1:]
    return '[' + snailstring + ']'

class SnailNumber():
    def __init__(self, string, parent=None):
        self.is_snailfish = '[' in string
        self.parent = parent
        if self.is_snailfish:
            l, r = split_snail(string)
            self.left = SnailNumber(l, self)
            self.right = SnailNumber(r, self)
        else:
            self.value = int(string)

    def __repr__(self):
        if self.is_snailfish:
            return '[' + repr(self.left) + ',' + repr(self.right) + ']'
        else:
            return str(self.value)

    def __add__(self, other):
        new = SnailNumber('[' + repr(self) + ',' + repr(other) + ']')
        new.reduce()
        return new

    def reduce(self):
        changed = True
        while changed:
            changed = self.fix_nesting()
            if not changed:
                changed = self.fix_split()

    def contains(self, other):
        if other == self:
            return True
        if self.is_snailfish:
            return self.left.contains(other) or self.right.contains(other)
        return False

    def add_right(self, value, origin):
        if origin == self:
            return False
        if self.is_snailfish:
            if not self.right.contains(origin):
                if self.left.add_right(value, origin):
                    return True
            if self.right.add_right(value, origin):
                return True
            if self.parent:
                return self.parent.add_right(value, self)
            return False
        self.value += value
        return True

    def add_left(self, value, origin):
        if origin == self:
            return False
        if self.is_snailfish:
            if not self.left.contains(origin):
                if self.right.add_left(value, origin):
                    return True
            if self.left.add_left(value, origin):
                return True
            if self.parent:
                return self.parent.add_left(value, self)
            return False
        self.value += value
        return True

    def fix_nesting(self, depth=1):
        if not self.is_snailfish:
            return False
        if depth > 4:
            l = self.left.value
            r = self.right.value
            self.value = 0
            self.is_snailfish = False
            self.parent.add_right(r, self)
            self.parent.add_left(l, self)
            return True
        if self.left.fix_nesting(depth+1):
            return True
        return self.right.fix_nesting(depth+1)

    def fix_split(self):
        if self.is_snailfish:
            if self.left.fix_split():
                return True
            return self.right.fix_split()
        if self.value >= 10:
            self.is_snailfish = True
            l =  self.value // 2
            r = self.value - l
            self.left = SnailNumber(str(l), self)
            self.right = SnailNumber(str(r), self)
            return True
        return False

    def get_magnitude(self):
        if self.is_snailfish:
            return 3*self.left.get_magnitude() + 2*self.right.get_magnitude()
        return self.value
        
def solve_star1():
    numbers = [*map(SnailNumber, read_file())]
    l = sum(numbers[1:], numbers[0])
    return l.get_magnitude()

def solve_star2():
    numbers = [*map(SnailNumber, read_file())]
    best = 0
    for first in numbers:
        for other in numbers:
            if first != other:
                best = max(best, (first + other).get_magnitude())
    return best



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
        print(solve_star1())
    elif star == 2:
        print(solve_star2())
