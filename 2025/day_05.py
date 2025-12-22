#! /usr/bin/python
import sys, getopt

class Range:
    def __init__(self, line):
        self.start, self.end = map(int,line.split("-"))

    def __contains__(self, ingredient):
        return self.start <= int(ingredient) <= self.end

    def combine(self, other):
        combined = False
        if self.start <= other.start <= self.end:
            self.end = max(self.end, other.end)
            combined = True
        if self.start <= other.end <= self.end:
            self.start = min(self.start, other.start)
            combined = True
        if self.start > other.start and self.end < other.end:
            self.start = other.start
            self.end = other.end
            combined = True
        return combined

    def count_ingredients(self):
        return self.end - self.start + 1


def solve_star1():
    find_ranges = True
    ranges = []

    fresh = []
    for line in read_file():
        if not line:
            find_ranges = False
            continue
        if find_ranges:
            ranges.append(Range(line))
        else:
            for range in ranges:
                if line in range:
                    fresh.append(line)
                    break

    return len(fresh)

def solve_star2():
    ranges = set()

    for line in read_file():
        if not line:
            break
        range = Range(line)
        remaining = set()
        for other in ranges:
            if not range.combine(other):
                remaining.add(other)
        ranges = remaining
        ranges.add(range)

    return sum(range.count_ingredients() for range in ranges)

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
