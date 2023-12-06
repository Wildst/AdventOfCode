#! /usr/bin/python
import sys, getopt

def expand_schematic( schematic ):
    schematic = [ "." + line + "." for line in schematic ]
    schematic = ["."*len(schematic[ 0 ] )] + schematic + ["."* len( schematic[ 0 ])]
    return schematic

def is_part_number( schematic, start_pos ):
    x, y = start_pos
    if not schematic[ y ][ x ].isdigit() or schematic[ y ][ x-1 ].isdigit():
        return False
    size = 0
    while schematic[ y ][ x + size ].isdigit():
        size += 1
    for test_y in range( y-1, y+2):
        for test_x in range( x - 1, x + size + 1 ):
            if not schematic[ test_y ][ test_x ].isdigit() and schematic[ test_y ][ test_x ] != ".":
                return True
    return False


def find_part_numbers( schematic ):
    numbers = []
    for y in range( 1, len( schematic ) - 1):
        for x in range( 1, len( schematic[ 0 ] ) - 1):
            if is_part_number( schematic, (x, y) ):
                size = 0
                while schematic[ y ][ x + size ].isdigit():
                    size += 1
                numbers.append( int( schematic[ y ][ x:x+size ] ))
    return numbers

def find_number_start( schematic, pos ):
    x, y = pos
    while schematic[ y ][ x - 1 ].isdigit():
        x -= 1
    return x, y

def find_adjacent_numbers( schematic, pos ):
    x, y = pos
    numbers = set()
    for i in range( x - 1, x + 2):
        for j in range( y - 1, y + 2 ):
            if schematic[ j ][ i ].isdigit():
                numbers.add( find_number_start( schematic, (i, j) ) )
    return numbers

def find_gears( schematic ):
    gears = []
    for y in range( 1, len( schematic ) - 1 ):
        for x in range( 1, len( schematic[ 0 ] ) - 1 ):
            if schematic[ y ][ x ] == "*":
                numbers = find_adjacent_numbers( schematic, ( x, y ) )
                if len( numbers ) == 2:
                    gear = 1
                    for i, j in numbers:
                        size = 0
                        while schematic[ j ][ i + size ].isdigit():
                            size += 1
                        gear *= int( schematic[ j ][ i:i+size] )
                    gears.append( gear )
    return gears

def solve_star1():
    schematic = [ "." + line + "." for line in read_file() ]
    schematic = ["."*len(schematic[ 0 ] )] + schematic + ["."* len( schematic[ 0 ])]

    numbers = find_part_numbers( schematic )
    return sum( numbers )

def solve_star2():
    schematic = expand_schematic( read_file() )
    gears = find_gears(schematic)
    return sum( gears )


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
