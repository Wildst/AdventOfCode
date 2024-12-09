#! /usr/bin/python
import sys, getopt

def parse_file_system( line ):
    empty = False
    identifier = 0
    file_system = []
    for amount in line:
        for i in range( int( amount ) ):
            if empty:
                file_system.append( -1 )
            else:
                file_system.append( identifier )
        if empty:
            identifier += 1
        empty = not empty
    return file_system

def compact_system( file_system ):
    front = 0
    back = len( file_system ) - 1
    while front <= back:
        while file_system[ front ] >= 0:
            front += 1
        while file_system[ back ] < 0:
            back -= 1

        if front < back:
            file_system[ front ], file_system[ back ] = file_system[ back ], file_system[ front ]
    return file_system

def get_checksum( file_system ):
    checksum = 0
    for i, value in enumerate( file_system ):
        if value > 0:
            checksum += i * value
    return checksum

def solve_star1():
    file_system = parse_file_system( read_file()[0] )
    compact_system( file_system )
    return get_checksum( file_system )

def solve_star2():
    free_blocks = []
    file_blocks = {}
    pos = 0
    for i, value in enumerate( read_file()[0] ):
        if i % 2:
            free_blocks.append( ( pos, int( value ) ) )
        else:
            file_blocks[ len( file_blocks ) ] = ( pos, int( value ) )
        pos += int( value )
    for i in range( len( file_blocks ) - 1, -1, -1 ):
        size = file_blocks[ i ][ 1 ]
        for j, free_block in enumerate( free_blocks ):
            if free_block[ 0 ] > file_blocks[ i ][ 0 ]:
                break
            if free_block[ 1 ] >= size:
                file_blocks[ i ] = (free_block[ 0 ], size )
                free_blocks[ j ] = ( free_block[ 0 ] + size, free_block[ 1 ] - size)
                break
    checksum = 0
    for file in file_blocks:
        startpos, size = file_blocks[ file ]
        for i in range( size ):
            checksum += file * ( startpos + i )
    return checksum


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
