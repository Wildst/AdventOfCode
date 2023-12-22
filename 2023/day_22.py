#! /usr/bin/python
import sys, getopt
from functools import total_ordering

@total_ordering
class Brick:
    def __init__( self, line, pos ):
        end1, end2 = [tuple( [*map( int, end.split(",") ) ]) for end in line.split("~")]
        self.end1 = ( min( end1[ 0 ], end2[ 0 ] ), min( end1[ 1 ], end2[ 1 ] ), min( end1[ 2 ], end2[ 2 ] ) )
        self.end2 = ( max( end1[ 0 ], end2[ 0 ] ), max( end1[ 1 ], end2[ 1 ] ), max( end1[ 2 ], end2[ 2 ] ) )

        self.name = ""
        while pos > 25:
            self.name = chr( ord("A") + pos % 26 ) + self.name
            pos //= 26
        self.name = chr( ord("A") + pos ) + self.name

    def get_blocks( self ):
        blocks = set()
        for x in range( self.end1[0], self.end2[0] + 1 ):
            for y in range( self.end1[1], self.end2[1] + 1 ):
                for z in range( self.end1[2], self.end2[2] + 1 ):
                    blocks.add( (x, y, z) )
        return blocks

    def move_down( self, amount=1):
        self.end1 = (self.end1[0], self.end1[1], self.end1[2] - amount)
        self.end2 = (self.end2[0], self.end2[1], self.end2[2] - amount)

    def move_up( self, amount=1):
        self.move_down( -amount )

    def fall( self, stack ):
        while self.end1[2] > 0 and not self.get_blocks().intersection(stack):
            self.move_down()
        self.move_up()

    def supports( self, brick ):
        if self.end2[2] + 1 != brick.end1[2]:
            return False
        self.move_up()
        test_blocks = self.get_blocks()
        self.move_down()
        return len( test_blocks.intersection( brick.get_blocks() ) ) > 0

    def __eq__( self, other ):
        return self.end1 == other.end1 and self.end2 == other.end2

    def __lt__( self, other ):
        return (self.end1[2], self.end2[2], self.end1, self.end2) < (other.end1[2], other.end2[2], other.end1, other.end2)

    def __repr__( self ):
        return self.name + ": " + repr( ( self.end1, self.end2 ) )

    def __hash__( self ):
        return hash( (self.end1, self.end2) )

def parse_file():
    return [ Brick( line, i ) for i, line in enumerate( read_file() ) ]

def solve_star1():
    bricks = sorted( parse_file() )
    stack = set()
    for brick in bricks:
        brick.fall(stack)
        stack = stack.union(brick.get_blocks())

    supported_by = {brick:[ other for other in bricks[ :i ] if other.supports( brick )  ] for i, brick in enumerate( bricks ) }
    options = set( bricks )
    for supports in supported_by.values():
        if len( supports ) == 1:
            if supports[ 0 ] in options:
                options.remove( supports[0])
    return len( options )

def solve_star2():
    bricks = sorted( parse_file() )
    stack = set()
    for brick in bricks:
        brick.fall(stack)
        stack = stack.union(brick.get_blocks())

    supported_by = {brick:set( other for other in bricks[ :i ] if other.supports( brick ) ) for i, brick in enumerate( bricks ) }

    result = 0
    for i, brick in enumerate( bricks ):
        fully_supported = set()
        fully_supported.add( brick )
        for other in bricks[i+1:]:
            if supported_by[ other ].issubset( fully_supported ) and len( supported_by[ other ] ) > 0:
                fully_supported.add( other )
        result += len( fully_supported ) - 1
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
