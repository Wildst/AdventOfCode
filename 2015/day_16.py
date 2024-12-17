#! /usr/bin/python
import sys, getopt

count_data = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
counts = { line.split()[0][:-1]: int( line.split()[ 1 ] ) for line in count_data.splitlines() }

print( counts)

def parse_data( line ):
    parts = line.split()
    return int( parts[1][:-1] ), { parts[ i ][:-1]: int( parts[ i+1 ].strip(",") ) for i in range( 2, len( parts ), 2 ) }

def solve_star1():
    aunts = [ parse_data( line ) for line in read_file() ]
    for aunt_nr, items in aunts:
        if len( [ item for item in items if items[ item ] == counts[ item  ] ] ) == len( items ):
            return aunt_nr
    return -1


def should_accept( item, amount ):
    if item in [ "cats", "trees" ]:
        return amount > counts[ item ]
    if item in [ "pomeranians", "goldfish" ]:
        return amount < counts[ item ]
    return amount == counts[ item ]

def solve_star2():
    aunts = [ parse_data( line ) for line in read_file() ]
    for aunt_nr, items in aunts:
        if len( [ item for item in items if should_accept( item, items[ item ] ) ]) == len( items ):
            return aunt_nr
    return -1


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
