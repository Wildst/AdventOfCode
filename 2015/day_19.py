#! /usr/bin/python
import sys, getopt
from functools import lru_cache

def solve_star1():
    replacements = [ ( line.split()[0], line.split()[-1] ) for line in read_file()[:-2] ]
    molecule = read_file()[-1]
    options = set()
    for original, replacement in replacements:
        for i in range( len( molecule ) ):
            if molecule[i:].startswith( original ):
                options.add( molecule[:i] + replacement + molecule[ i+len(original):])
    return len( options )

def get_replacement_value( replacement ):
    return len([ c for c in replacement[-1] if c.isupper() ] )

class Solver:
    def __init__( self, replacements ):
        self.replacements = sorted( replacements, key=get_replacement_value, reverse=True )
        self.checked = {}
        for original, replacement in self.replacements:
            if original == "e":
                self.checked[ replacement ] = 1

        self.best = 1000

    def solve( self, target, depth = 0 ):
        if target in self.checked:
            return self.checked[ target ] + depth
        if depth >= self.best:
            print( target, depth )
            return 10000
        best = 1000
        for original, replacement in self.replacements:
            if original == "e":
                continue
            i = target.find( replacement )
            if i >= 0:
                test = self.solve( target[:i] + original + target[ i+len(replacement):], depth + 1 )
                if test < self.best:
                    self.best = test
                    print( self.best ) # For my input, the first time this ocurred, it was already the best option
                best = min( best, test )
        self.checked[ target ] = best - depth
        if len( self.checked ) % 1000000 == 0:
            print( len( self.checked ), target )
        return best



def solve_star2():
    solver = Solver( [ ( line.split()[0], line.split()[-1] ) for line in read_file()[:-2] ] )
    target = read_file()[-1]
    return solver.solve( target )


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
