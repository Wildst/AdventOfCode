#! /usr/bin/python
import sys, getopt

DIRECTIONS = [
    ( 0, 1 ),
    ( 1, 0 ),
    ( 0,-1 ),
    (-1, 0 )
]

def is_valid( farm, pos ):
    x, y = pos
    return 0 <= x < len( farm[ 0 ] ) and 0 <= y < len( farm )

def get_region( farm, pos ):
    todo = set()
    plot_type = farm[pos[1]][pos[0]]
    result = set()
    todo.add( pos )
    while todo:
        x, y = todo.pop()
        if not is_valid( farm, (x,y) ) or farm[y][x] != plot_type:
            continue
        if (x,y) not in result:
            for dx, dy in DIRECTIONS:
                todo.add( ( x+dx, y+dy ) )
        result.add( (x, y) )
    return result

def get_region_area( region ):
    return len(region)

def get_region_perimeter( region ):
    result = 0
    for x,y in region:
        for dx,dy in DIRECTIONS:
            if (x+dx, y+dy) not in region:
                result += 1
    return result

def get_region_sides( region ):
    result = 0
    for x,y in region:
        for i, direction in enumerate(DIRECTIONS):
            dx,dy = direction
            if (x+dx, y+dy) not in region:
                px, py = DIRECTIONS[ i - 1 ]
                if (x+px, y+py) not in region or (x+dx+px,y+dy+py) in region:
                    result += 1
    return result

def solve_star1():
    farm = read_file()
    todo = set( (x,y) for y in range( len( farm ) ) for x in range( len( farm[0] ) ) )
    regions = []
    while todo:
        pos = todo.pop()
        new_region = get_region( farm, pos )
        for plot in new_region:
            if plot in todo:
                todo.remove( plot )
        regions.append( new_region )

    return sum( get_region_area( region ) * get_region_perimeter( region ) for region in regions )

def solve_star2():
    farm = read_file()
    todo = set( (x,y) for y in range( len( farm ) ) for x in range( len( farm[0] ) ) )
    regions = []
    while todo:
        pos = todo.pop()
        new_region = get_region( farm, pos )
        for plot in new_region:
            if plot in todo:
                todo.remove( plot )
        regions.append( new_region )

    return sum( get_region_area( region ) * get_region_sides( region ) for region in regions )


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
