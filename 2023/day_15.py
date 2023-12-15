#! /usr/bin/python
import sys, getopt

class Lens:
    def __init__( self, label, focal_length ):
        self.focal_length = focal_length
        self.label = label

    def replace( self, new_focal_length ):
        self.focal_length = new_focal_length

class Box:
    def __init__(self):
        self.lenses = []

    def add( self, new_lens ):
        for lens in self.lenses:
            if new_lens.label == lens.label:
                lens.replace( new_lens.focal_length )
                return
        self.lenses.append( new_lens )

    def remove( self, label ):
        for lens in self.lenses:
            if lens.label == label:
                self.lenses.remove( lens )

    def get_power( self ):
        result = 0
        for pos, lens in enumerate( self.lenses ):
            result += ( pos+1 ) * lens.focal_length
        return result

def hash( string ):
    value = 0
    for c in string:
        value += ord( c )
        value *= 17
        value %= 256
    return value

def solve_star1():
    return sum( map( hash, read_file()[0].split(",") ) )

def solve_star2():
    boxes = [ Box() for _ in range(256) ]
    for instruction in read_file()[0].split(","):
        if "-" in instruction:
            label = instruction[:-1]
            box = hash( label )
            boxes[box].remove( label )
        else:
            label = instruction[:-2]
            boxes[ hash( label ) ].add( Lens( label, int( instruction[ -1 ] ) ) )
    result = 0
    for pos, box in enumerate( boxes ):
        result += (pos+1)* box.get_power()
    return result


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
