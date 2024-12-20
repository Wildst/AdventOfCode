#! /usr/bin/python
import sys, getopt

DIRECTIONS = [
    ( 1, 0 ),
    ( 0, 1 ),
    (-1, 0 ),
    ( 0,-1 )
]

class Track:
    def __init__( self, data ):
        for y, line in enumerate( data ):
            for x, state in enumerate( line ):
                if state == "S":
                    self.start = (x,y)
                elif state == "E":
                    self.end = (x,y)
        self.track = data

    def get_start( self ):
        return self.start

    def get_end( self ):
        return self.end

    def is_wall( self, pos ):
        x, y = pos
        return self.track[ y ][ x ] == "#"

    def get_dimensions( self ):
        return len( self.track[ 0 ] ), len( self.track )

    def is_valid( self, pos ):
        x, y = pos
        return 0 <= x < len( self.track[ 0 ] ) and 0 <= y < len( self.track )

def get_times( track: Track ):
    max_x, max_y = track.get_dimensions()
    times = [ [ max_x * max_y for _ in range( max_x ) ] for _ in range( max_y ) ]
    x, y = track.get_start()
    times[ y ][ x ] = 0
    todo = set()
    todo.add( track.get_start() )
    while todo:
        x, y = todo.pop()
        for dx, dy in DIRECTIONS:
            if not track.is_wall( ( x+dx, y+dy ) ) and times[ y+dy ][ x+dx ] > times[ y ][ x ] + 1 :
                times[ y+dy ][ x+dx ] = times[ y ][ x ] + 1
                todo.add( ( x+dx, y+dy ) )
    return times

def get_cheats( track: Track, time ):
    max_x, max_y = track.get_dimensions()
    cheats = set()
    for x in range( max_x ):
        for y in range( max_y ):
            if track.is_wall( ( x, y ) ):
                continue
            for neighbour in [ ( x+dx, y+dy ) for dx in range ( -time, time+1 ) for dy in range( -time+abs( dx ), time-abs(dx)+1 ) ]:
                if track.is_valid( neighbour ) and not track.is_wall( neighbour ):
                    cheats.add( ( ( x, y ), neighbour ) )
    return cheats

def get_neighbours( pos, track ):
    x, y = pos
    return [ (x+dx, y+dy) for dx,dy in DIRECTIONS if track.is_valid( ( x+dx, y+dy ) ) ]

def get_cheat_score( cheat, track: Track, times ):
    diff = abs( cheat[ 0 ][ 0 ] - cheat[ 1 ][ 0 ] ) + abs( cheat[ 0 ][ 1 ] - cheat[ 1 ][ 1 ] )
    score = max( 0, times[ cheat[1][1] ][ cheat[1][0] ] - times[ cheat[0][1] ][ cheat[0][0] ] - diff )
    if score == 71:
        print( cheat, score, times[ cheat[1][1] ][ cheat[1][0] ], times[ cheat[0][1] ][ cheat[0][0] ], diff )
    return score

def solve_star1():
    track = Track( read_file() )
    times = get_times( track )
    cheats = get_cheats( track, 2 )
    scores = {}
    for cheat in cheats:
        score = get_cheat_score( cheat, track, times )
        if score not in scores:
            scores[ score ] = 0
        scores[ score ] += 1
    return sum( scores[ score ] for score in scores if score >= 100 )


def solve_star2():
    track = Track( read_file() )
    times = get_times( track )
    cheats = get_cheats( track, 20 )
    scores = {}
    for cheat in cheats:
        score = get_cheat_score( cheat, track, times )
        if score not in scores:
            scores[ score ] = 0
        scores[ score ] += 1
    return sum( scores[ score ] for score in scores if score >= 100 )


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
