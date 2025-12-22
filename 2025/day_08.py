#! /usr/bin/python
import sys, getopt
from functools import reduce

class Circuit:
    def __init__(self):
        self.boxes = set()

    def add(self, box):
        self.boxes.add(box)

    def merge(self, other):
        if other == self:
            return
        for box in other.boxes:
            box.circuit = self
            self.boxes.add(box)

    def count(self):
        return len(self.boxes)

    def __repr__(self):
        return "Circuit (%i):\n\t%s\n" % (len(self.boxes), "\n\t".join(map(repr,self.boxes)))

class Box:
    def __init__(self, line):
        self.x, self.y, self.z = [*map(int,line.split(","))]
        self.circuit = Circuit()
        self.circuit.add(self)

    def __repr__(self):
        return "Box(%i, %i, %i)" %(self.x, self.y, self.z)

    def distance(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)**.5

def solve_star1(connection_count):
    boxes = [*map(Box, read_file())]
    combinations = []
    for i, box in enumerate(boxes[:-1]):
        for other in boxes[i+1:]:
            combinations.append((box, other))
    combinations = sorted(combinations, key=lambda combination: combination[0].distance(combination[1]))

    for combination in combinations[:connection_count]:
        first, second = combination
        first.circuit.merge(second.circuit)
    circuits = sorted(set([box.circuit for box in boxes]), key=lambda circuit: circuit.count())
    result = 1
    for circuit in circuits[-3:]:
        result *= circuit.count()
    return result

def solve_star2():
    boxes = [*map(Box, read_file())]
    combinations = []
    for i, box in enumerate(boxes[:-1]):
        for other in boxes[i+1:]:
            combinations.append((box, other))
    combinations = sorted(combinations, key=lambda combination: combination[0].distance(combination[1]))

    for combination in combinations:
        first, second = combination
        if first.circuit == second.circuit:
            continue
        first.circuit.merge(second.circuit)
        if len(set([box.circuit for box in boxes])) == 1:
            return first.x * second.x


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][0:-2] + "in"
    file_dir = "input_files"
    connections = 1000
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
            connections = 10
            file_dir = "test_files"

    if star == 1:
        print(solve_star1(connections))
    elif star == 2:
        print(solve_star2())
