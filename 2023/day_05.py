#! /usr/bin/python
import sys, getopt

class Range:
    def __init__( self, line ):
        parts = [*map( int, line.split() )]
        self.start = parts[ 1 ]
        self.size = parts[ 2 ]
        self.offset = parts[ 0 ] - parts[ 1 ]

    def is_in_range( self, id ):
        return self.start <= id < self.start + self.size

    def get_mapped_value( self, id ):
        return id + self.offset

class Mapping:
    def __init__(self, lines, origin, destination ):
        self.origin = origin
        self.destination = destination
        self.ranges = []
        for line in lines:
            self.ranges.append( Range(line) )

    def get_range_for_id( self, id ):
        for range in self.ranges:
            if range.is_in_range( id ):
                return range
        return None

    def get_next_range_start( self, id ):
        next = 0
        for range in self.ranges:
            if id < range.start < next:
                next = range.start
        return next

    def get_mapped_value( self, id ):
        for range in self.ranges:
            if range.is_in_range( id ):
                return range.get_mapped_value( id )
        return id

    def get_mapped_range( self, start_range ):
        result = []
        for start, size in start_range:
            while size > 0:
                range = self.get_range_for_id( start )
                if range:
                    distance = range.size - ( start - range.start )
                    distance = min( distance, size )
                    result.append( ( range.get_mapped_value( start ), distance ) )
                    size -= distance
                    start += distance
                else:
                    next = self.get_next_range_start( start )
                    if next:
                        distance = next - start
                        distance = min( distance, size )
                        result.append( ( start, distance ) )
                        size -= distance
                        start += distance
                    else:
                        result.append( ( start, size ) )
                        size = 0
        return result


def get_mappings():
    lines = read_file()

    mappings = []

    current_map = []
    origin = ""
    destination = ""
    for line in lines[ 2: ]:
        if not line:
            if current_map:
                mappings.append( Mapping( current_map, origin, destination ) )
            current_map = []
            origin = ""
            destination = ""
        elif line.endswith( "map:" ):
            origin, _, destination = line.split()[ 0 ].split("-")
        else:
            current_map.append( line )
    if current_map:
        mappings.append( Mapping( current_map, origin, destination ) )
    return mappings


def solve_star1():
    mappings = get_mappings()
    values = [ *map( int, read_file()[ 0 ].split(":")[ 1 ].split() ) ]

    current = "seed"
    while current != "location":
        for mapping in mappings:
            if mapping.origin == current:
                values = [*map( mapping.get_mapped_value, values )]
                current = mapping.destination
                break
    return min( values )

def solve_star2():
    mappings = get_mappings()
    seeds = [ *map( int, read_file()[ 0 ].split(":")[ 1 ].split() ) ]
    ranges = []
    for i in range(0, len( seeds), 2 ):
        ranges.append( ( seeds[ i ], seeds[ i + 1 ] ) )

    current = "seed"
    while current != "location":
        print( ranges )
        for mapping in mappings:
            if mapping.origin == current:
                ranges = mapping.get_mapped_range( ranges )
                current = mapping.destination
                break
    closest = ranges[ 0 ][ 0 ]
    for r in ranges:
        closest = min( closest, r[ 0 ] )
    return closest


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
