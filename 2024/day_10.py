#! /usr/bin/python
import sys, getopt

DIRECTIONS = {
    (  0,  1 ),
    (  1,  0 ),
    (  0, -1 ),
    ( -1,  0 )
}

def is_valid( land, pos ):
    x, y = pos
    return 0 <= x < len( land[ 0 ] ) and 0 <= y < len( land[ 1 ] )

def get_land( data ):
    return [ [ int( c ) if c != "." else 10 for c in line ] for line in data ]

def get_possibilities( land ):
    todo = set( (x, y) for y in range(len(land)) for x in range(len(land[0])) if land[ y ][ x ] == 9 )
    reachable = [ [ set() for _ in range( len( row ) ) ] for row in land ]
    while todo:
        x, y = todo.pop()
        if land[ y ][ x ] == 9:
            if len( reachable[ y ][ x ] ) != 1:
                reachable[ y ][ x ].add( (x,y) )
                for dx, dy in DIRECTIONS:
                    if is_valid( land, ( x+dx, y+dy ) ):
                        todo.add( (x+dx, y+dy) )
        else:
            size = len( reachable[ y ][ x ] )
            for dx, dy in DIRECTIONS:
                if is_valid( land, ( x+dx, y+dy ) ) and land[ y ][ x ] + 1 == land[ y+dy ][ x+dx ]:
                    for position in reachable[ y+dy ][ x+dx ]:
                        reachable[ y ][ x ].add( position )

            if size != len( reachable[ y ][ x ] ):
                for dx, dy in DIRECTIONS:
                    if is_valid( land, ( x+dx, y+dy ) ):
                        todo.add( (x+dx, y+dy) )
    return reachable

def count_ways( land ):
    todo = set( (x, y) for y in range(len(land)) for x in range(len(land[0])) if land[ y ][ x ] == 9 )
    ways = [ [ 0 for _ in range( len( row ) ) ] for row in land ]
    while todo:
        x, y = todo.pop()
        if land[ y ][ x ] == 9:
            if ways[ y ][ x ] != 1:
                ways[ y ][ x ] = 1
                for dx, dy in DIRECTIONS:
                    if is_valid( land, ( x+dx, y+dy ) ):
                        todo.add( (x+dx, y+dy) )
        else:
            size = ways[ y ][ x ]
            ways[ y ][ x ] = 0
            for dx, dy in DIRECTIONS:
                if is_valid( land, ( x+dx, y+dy ) ) and land[ y ][ x ] + 1 == land[ y+dy ][ x+dx ]:
                    ways[ y ][ x ] += ways[ y+dy ][ x+dx ]

            if size != ways[ y ][ x ]:
                for dx, dy in DIRECTIONS:
                    if is_valid( land, ( x+dx, y+dy ) ):
                        todo.add( (x+dx, y+dy) )
    return ways

def get_score( land, counts ):
    score = 0
    for y in range( len( land ) ):
        for x in range( len( land[ 0 ] ) ):
            if land[ y ][ x ] == 0:
                score += len( counts[ y ][ x ] )
    return score

def solve_star1():
    land = get_land( read_file() )
    counts = get_possibilities( land )
    return get_score( land, counts )

def solve_star2():
    land = get_land( read_file() )
    counts = count_ways( land )
    score = 0
    for y in range( len( land ) ):
        for x in range( len( land[ 0 ] ) ):
            if land[ y ][ x ] == 0:
                score += counts[ y ][ x ]
    return score


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
