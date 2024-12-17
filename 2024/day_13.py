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

factor = 2

def get_close( button_a, button_b, prize ):
    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize

    current_x, current_y = 0, 0
    score = 0

    while p_x - current_x > 100:
        t_x, t_y = ( p_x - current_x ) // factor, ( p_y - current_y ) // factor
        partial_score, c_x, c_y = get_close( button_a, button_b, (t_x, t_y) )
        partial_score *= factor
        if not partial_score:
            break
        c_x *= factor
        c_y *= factor
        score += partial_score

        current_x += c_x
        current_y += c_y

    c_x = current_x
    c_y = current_y

    return score, c_x, c_y

def get_far_prize( button_a, button_b, prize ):
    a_x, a_y = button_a
    b_x, b_y = button_b
    p_x, p_y = prize

    p_x += 10000000000000
    p_y += 10000000000000

    determinant = a_x * b_y - a_y * b_x

    if (p_x * b_y - p_y * b_x ) % determinant or (a_x * p_y - a_y * p_x ) % determinant:
        return 0

    a_count = (p_x * b_y - p_y * b_x ) / determinant
    b_count = (a_x * p_y - a_y * p_x ) / determinant

    if a_count < 0 or b_count < 0:
        return 0

    return int( a_count * 3 + b_count )

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
