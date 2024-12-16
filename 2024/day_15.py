#! /usr/bin/python
import sys, getopt

DIRECTIONS = {
    ">": ( 1, 0 ),
    "<": (-1, 0 ),
    "^": ( 0,-1 ),
    "v": ( 0, 1 )
}

def parse_input( data ):
    position = ( -1, -1 )
    boxes = set()
    walls = set()
    moves = ""

    i = 0
    while data[i]:
        for j, item in enumerate( data[ i ] ):
            if item == "#":
                walls.add( ( j, i ) )
            elif item == "O":
                boxes.add( ( j, i ) )
            elif item == "@":
                position = ( j, i )
        i += 1

    moves = "".join( data[i:] )
    return position, boxes, walls, moves

def parse_input_wide( data ):
    position = ( -1, -1 )
    boxes = set()
    walls = set()
    moves = ""

    i = 0
    while data[i]:
        for j, item in enumerate( data[ i ] ):
            if item == "#":
                walls.add( ( j*2, i ) )
                walls.add( ( j*2+1, i ) )
            elif item == "O":
                boxes.add( ( j*2, i ) )
            elif item == "@":
                position = ( j*2, i )
        i += 1

    moves = "".join( data[i:] )
    return position, boxes, walls, moves

def do_move( position, boxes, walls, move ):
    dx, dy = DIRECTIONS[ move ]
    x, y = position
    box_count = 0
    while ( x+dx + dx*box_count, y+dy + dy*box_count ) in boxes:
        box_count += 1
    if ( x+dx + dx*box_count, y+dy + dy*box_count ) in walls:
        # nothing happens
        return position, boxes
    position = x+dx, y+dy
    if box_count:
        boxes.remove( ( x+dx,y+dy ) )
        boxes.add( (x+dx*(box_count+1),y+dy*(box_count+1) ) )
    return position, boxes

def do_wide_move( position, boxes, walls, move ):
    dx, dy = DIRECTIONS[ move ]
    x, y = position
    moving_boxes = []
    positions_to_check = []
    positions_to_check.append( ( x+dx, y+dy ) )
    i = 0
    while i < len( positions_to_check ):
        cx, cy = positions_to_check[ i ]
        if ( cx, cy ) in walls:
            # movement blocked
            return position, boxes
        if ( cx, cy ) in boxes and ( cx, cy ) not in moving_boxes:
            moving_boxes.append( ( cx, cy ) )
            if (cx+dx, cy+dy) not in positions_to_check:
                positions_to_check.append( (cx+dx, cy+dy) )
            if (cx+dx+1, cy+dy) not in positions_to_check:
                positions_to_check.append( (cx+dx+1, cy+dy) )
        if ( cx-1, cy ) in boxes and ( cx-1, cy ) not in moving_boxes:
            moving_boxes.append( ( cx-1, cy ) )
            if (cx-1+dx, cy+dy) not in positions_to_check:
                positions_to_check.append( (cx-1+dx, cy+dy) )
            if (cx-1+dx+1, cy+dy) not in positions_to_check:
                positions_to_check.append( (cx-1+dx+1, cy+dy) )
        i += 1
    position = x+dx, y+dy
    for bx, by in moving_boxes[::-1]:
        boxes.remove( ( bx, by ) )
        boxes.add( ( bx+dx, by+dy ) )
    return position, boxes

def get_GPS( box ):
    return box[ 0 ] + 100*box[ 1 ]

def print_warehouse( position, walls, boxes ):
    width, height = 0, 0
    for wall in walls:
        width = max( width, wall[ 0 ] + 1 )
        height = max( height, wall[ 1 ] + 1 )
    warehouse = [ [ "." for _ in range( width ) ] for _ in range( height ) ]
    for wx, wy in walls:
        warehouse[ wy ][ wx ] = "#"
    for bx, by in boxes:
        warehouse[ by ][ bx ] = "O"
    warehouse[ position[1] ][ position[0] ] = "@"

    print()
    for line in warehouse:
        print( "".join( line ) )

def print_scaled_warehouse( position, walls, boxes ):
    width, height = 0, 0
    for wall in walls:
        width = max( width, wall[ 0 ] + 1 )
        height = max( height, wall[ 1 ] + 1 )
    warehouse = [ [ "." for _ in range( width ) ] for _ in range( height ) ]
    for wx, wy in walls:
        warehouse[ wy ][ wx ] = "#"
    for bx, by in boxes:
        warehouse[ by ][ bx ] = "["
        warehouse[ by ][ bx + 1] = "]"
    warehouse[ position[1] ][ position[0] ] = "@"

    print()
    for line in warehouse:
        print( "".join( line ) )


def solve_star1():
    position, boxes, walls, moves = parse_input( read_file() )
    for move in moves:
        position, boxes = do_move( position, boxes, walls, move )
    return sum( get_GPS( box ) for box in boxes )


def solve_star2():
    position, boxes, walls, moves = parse_input_wide( read_file() )
    for move in moves:
        position, boxes = do_wide_move( position, boxes, walls, move )
    return sum( get_GPS( box ) for box in boxes )


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
