#! /usr/bin/python
import sys, getopt

def parse_location( line ):
    parts = line.split(" ")
    return (int( parts[-2][2:-1] ), int( parts[ -1 ][2:] ) )

def parse_prize( data ):
    a = parse_location( data[ 0 ] )
    b = parse_location( data[ 1 ] )
    prize = parse_location( data[ 2 ] )
    return a, b, prize

def parse_prizes( data ):
    prizes = []
    lines = []
    for line in data:
        if not line:
            prizes.append( parse_prize( lines ))
            lines = []
        else:
            lines.append( line )
    if lines:
        prizes.append( parse_prize( lines ) )
    return prizes

def get_prize( button_a, button_b, prize ):
    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize
    best = 999999
    for i in range(101):
        if ( p_x - a_x * i ) % b_x == 0:
            b_count = ( p_x - a_x * i ) // b_x
            if p_y - a_y * i == b_y * b_count and b_count <= 100:
                best = min( best, i*3 + b_count )
    if best < 999999:
        return best
    return 0

def solve_star1():
    return sum( get_prize(*machine) for machine in parse_prizes( read_file() ) )


def get_far_prize( button_a, button_b, prize ):
    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize
    p_x += 10000000000000
    p_y += 10000000000000
    a_factor = a_x / a_y
    b_factor = b_x / b_y
    p_factor = p_x / p_y
    c_x, c_y = 0, 0
    score = 0
    while c_x < p_x:
        if c_x % 100000000000 == 0:
            print( c_x, c_y )
        c_factor = c_x / c_y if c_y else 1
        if c_factor < p_factor:
            if a_factor > p_factor:
                score += 3
                c_x += a_x
                c_y += a_y
            else:
                score += 1
                c_x += b_x
                c_y += b_y
        else:
            if a_factor < p_factor:
                score += 3
                c_x += a_x
                c_y += a_y
            else:
                score += 1
                c_x += b_x
                c_y += b_y
    return score if c_x == p_x and c_y == p_y else 0

def solve_star2():
    return sum( get_far_prize(*machine) for machine in parse_prizes( read_file() ) )



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
