#! /usr/bin/python
import sys, getopt

left = (-1, 0)
top = (0, -1)
right = (1, 0)
bottom= (0, 1)
directions = [left, top, right, bottom]

def get_other_directions( direction ):
    if direction == left or direction == right:
        return (top, bottom)
    return (left, right)

def in_grid( pos, grid ):
    x, y = pos
    return 0 <= x < len( grid[ 0 ] ) and 0 <= y < len( grid )

def solve_star1():
    weights = [[ int( c ) for c in line ] for line in read_file() ]
    distances = [[ { direction: 10*len(weights) * len(weights[0]) for direction in directions } for _ in weights[0] ] for _ in weights ]

    distances[ 0 ][ 0 ] = { direction: 0 for direction in directions }
    work_list = [ ( (0, 0), direction ) for direction in directions ]
    while work_list:
        pos, direction = work_list[ 0 ]
        x, y = pos
        work_list = work_list[1:]
        start_value = distances[ y ][ x ][ direction ]
        for dx, dy in get_other_directions( direction ):
            current_value = start_value
            for i in range( 1, 4 ):
                if not in_grid( (x+i*dx, y+i*dy), weights ):
                    break
                current_value += weights[y+i*dy][ x+i*dx ]
                if distances[ y+i*dy ][x+i*dx][(dx, dy)] > current_value:
                    work_list.append(((x+i*dx, y+i*dy), (dx, dy)))
                    distances[ y+i*dy][x+i*dx][(dx, dy)] = current_value
    best = min( distances[ -1 ][ -1 ][ direction ] for direction in directions )
    return best
def solve_star2():
    weights = [[ int( c ) for c in line ] for line in read_file() ]
    distances = [[ { direction: 10*len(weights) * len(weights[0]) for direction in directions } for _ in weights[0] ] for _ in weights ]

    distances[ 0 ][ 0 ] = { direction: 0 for direction in directions }
    work_list = [ ( (0, 0), direction ) for direction in directions ]

    while work_list:
        pos, direction = work_list[ 0 ]
        x, y = pos
        work_list = work_list[1:]
        start_value = distances[ y ][ x ][ direction ]
        for dx, dy in get_other_directions( direction ):
            current_value = start_value
            for i in range( 1, 11 ):
                if not in_grid( (x+i*dx, y+i*dy), weights ):
                    break
                current_value += weights[y+i*dy][ x+i*dx ]
                if i > 3 and distances[ y+i*dy ][x+i*dx][(dx, dy)] > current_value:
                    work_list.append(((x+i*dx, y+i*dy), (dx, dy)))
                    distances[ y+i*dy][x+i*dx][(dx, dy)] = current_value
    best = min( distances[ -1 ][ -1 ][ direction ] for direction in directions )
    return best


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
