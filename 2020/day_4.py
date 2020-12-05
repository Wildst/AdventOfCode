#! /usr/bin/python
import sys, getopt, re

HAIR_COLOR_MATCH = re.compile("^#[0-9a-f]{6}$")

class Passport:
    def __init__(self, elements):
        self.elements = {}
        for element in elements:
            key, value = element.split(":")
            self.elements[key] = value

    def is_complete(self):
        for requirement in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if requirement not in self.elements.keys():
                return False

        return True

    def number_limit(self, value, lower, upper, l=4):
        if not value.isnumeric() or len(value) != l or not lower <= int(value) <= upper:
            return False
        return True

    def is_valid(self):
        if not self.is_complete():
            return False

        correct = True
        # Check years
        correct &= self.number_limit(self.elements["byr"], 1920, 2002)
        correct &= self.number_limit(self.elements["iyr"], 2010, 2020)
        correct &= self.number_limit(self.elements["eyr"], 2020, 2030)

        # Check heigth
        heigth = self.elements["hgt"]
        if heigth[-2:] == "cm":
            correct &= self.number_limit(heigth[:-2], 150, 193, l=3)
        elif heigth[-2:] == "in":
            correct &= self.number_limit(heigth[:-2], 59, 76, l=2)
        else:
            correct = False

        # Check hair color
        correct &= bool(HAIR_COLOR_MATCH.match(self.elements["hcl"]))

        # Check eye color
        correct &= self.elements["ecl"] in "amb blu brn gry grn hzl oth"

        # Check pid
        correct &= len(self.elements["pid"]) == 9 and self.elements["pid"].isnumeric()

        return correct

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


def solve_star1():
    passports = []
    tmp_data = ""
    for line in read_file():
        if not line:
            passports.append(Passport(tmp_data.split(" ")))
            tmp_data = ""
        else:
            if not tmp_data:
                tmp_data = line
            else:
                tmp_data += " " + line
    if tmp_data:
        passports.append(Passport(tmp_data.split(" ")))
        tmp_data = ""

    print(len([ p for p in passports if p.is_complete()]))


def solve_star2():
    passports = []
    tmp_data = ""
    for line in read_file():
        if not line:
            passports.append(Passport(tmp_data.split(" ")))
            tmp_data = ""
        else:
            if not tmp_data:
                tmp_data = line
            else:
                tmp_data += " " + line
    if tmp_data:
        passports.append(Passport(tmp_data.split(" ")))
        tmp_data = ""

    print(len([ p for p in passports if p.is_valid()]))




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









