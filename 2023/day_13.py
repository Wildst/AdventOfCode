#! /usr/bin/python
import sys, getopt

def find_reflections(line):
    result = set()
    for i in range( 1, len(line) ):
        s = min( i, len(line) - i)
        if line[:i][::-1][:s] == line[i:][:s]:
            result.add( i )
    return result

def find_reflection( grid, ignore_row=0, ignore_column=0 ):
    rows = 0
    columns = 0
    reflections = set(i for i in range(len(grid[0])))
    reflections.remove( ignore_column )
    for line in grid:
        reflections = reflections.intersection( find_reflections( line ) )
    if reflections:
        columns = sum( reflections )
    reflections = set(i for i in range(len(grid)))
    reflections.remove( ignore_row )
    for i in range( len( grid[0] ) ):
        reflections = reflections.intersection(find_reflections( "".join([line[ i ] for line in grid ] ) ) )
    if reflections:
        rows = sum( reflections )
    return rows, columns

def get_grid_score( grid ):
    row, column = find_reflection( grid )
    return column + row * 100

def solve_star1():
    total = 0
    grid = []
    for line in read_file():
        if line:
            grid.append( line )
        else:
            total += get_grid_score( grid )
            grid = []
    total += get_grid_score( grid )
    return total

def repair_mirror_score( grid ):
    score = 0
    original_row, original_column = find_reflection( grid )
    for y in range( len( grid ) ):
        for x in range( len( grid[ 0 ] ) ):
            test_grid = [ line for line in grid ]
            test_grid[ y ] = test_grid[y][:x]+ ("#" if grid[ y ][ x ] == "." else ".") + test_grid[ y ][x+1:]
            row, column = find_reflection( test_grid, original_row, original_column )
            if row:
                return 100*row
            if column:
                return column
    return score

def solve_star2():
    total = 0
    grid = []
    for line in read_file():
        if line:
            grid.append( line )
        else:
            total += repair_mirror_score( grid )
            grid = []
    total += repair_mirror_score( grid )
    return total


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
