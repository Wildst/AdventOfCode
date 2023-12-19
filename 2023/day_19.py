#! /usr/bin/python
import sys, getopt

class Rule():
    def __init__( self, line ):
        if ":" in line:
            req, self.dest = line.split(":")
            value = int( req[2:] )
            self.filter = lambda part: part[ req[ 0 ] ] < value if req[1] == "<" else part[ req[ 0 ] ] > value
        else:
            self.dest = line
            self.filter = lambda _: True

class WorkFlow():
    def __init__( self, line ):
        self.name, line = line.split( "{" )
        line = line[ :-1 ]
        self.rules = []
        for rule in line.split(","):
            self.rules.append( Rule( rule ) )

    def accepts( self, part, workflows ):
        for rule in self.rules:
            if rule.filter( part ):
                if rule.dest == "A":
                    return True
                if rule.dest == "R":
                    return False
                return workflows[ rule.dest ].accepts( part, workflows )

def parse_part( line ):
    result = {}
    for part in line[1:-1].split(","):
        category, score = part.split( "=" )
        result[ category ] = int( score )
    return result

def part_value( part ):
    return sum( part.values() )

def solve_star1():
    lines = read_file()
    pos = 0
    workflows = {}
    while lines[ pos ]:
        flow = WorkFlow( lines[ pos ] )
        workflows[ flow.name ] = flow
        pos += 1
    return sum( sum( parse_part( line ).values() ) for line in lines[ pos+1: ] if workflows["in"].accepts( parse_part( line ), workflows ))

def solve_star2():
    lines = read_file()
    pos = 0
    workflows = {}
    while lines[ pos ]:
        flow = WorkFlow( lines[ pos ] )
        workflows[ flow.name ] = flow
        pos += 1
    return 0


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
