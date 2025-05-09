#! /usr/bin/python
import sys, getopt
from functools import lru_cache

KEYPAD = [ "789", "456", "123", " 0A" ]

REMOTE = [ " ^A", "<v>" ]



def find_button_position( button, keypad = KEYPAD ):
    for y, row in enumerate( keypad ):
        for x, option in enumerate( row ):
            if option == button:
                return x, y
    print( "Invalid Button:", button)
    return 0,0

def get_all_paths( start, end, keypad ):
    x, y = start
    if start == end:
        return [ "A" ]
    if keypad[ y ][ x ] == " ":
        return []
    options = []
    if x < end[ 0 ]:
        for option in get_all_paths( (x+1, y), end, keypad ):
            options.append( ">" + option )
    if x > end[ 0 ]:
        for option in get_all_paths( (x-1, y), end, keypad ):
            options.append( "<" + option )
    if y < end[ 1 ]:
        for option in get_all_paths( (x, y+1), end, keypad ):
            options.append( "v" + option )
    if y > end[ 1 ]:
        for option in get_all_paths( (x, y-1), end, keypad ):
            options.append( "^" + option )
    return options


@lru_cache
def get_shortest_path( start, end, is_keypad=False ):
    result = ""
    s_x, s_y = start
    e_x, e_y = end
    keypad = KEYPAD if is_keypad else REMOTE

    if keypad[ s_y ][ e_x ] == " " or keypad[ e_y ][ s_x ] == " ":
        if keypad == REMOTE:
            while s_y < e_y:
                s_y += 1
                result += "v"
            while s_x < e_x:
                s_x += 1
                result += ">"
        else:
            while s_x < e_x:
                s_x += 1
                result += ">"
            while s_y > e_y:
                s_y -= 1
                result += "^"
    while s_x > e_x:
        s_x -= 1
        result += "<"
    while s_y < e_y:
        s_y += 1
        result += "v"
    while s_y > e_y:
        s_y -= 1
        result += "^"
    while s_x < e_x:
        s_x += 1
        result += ">"
    return result + "A"

def calculate_presses( code, keypad ):
    presses = ""
    position = find_button_position( "A", keypad )
    for button in code:
        target = find_button_position( button, keypad )
        presses += get_shortest_path( position, target, keypad == KEYPAD )
        position = target
    return presses

def get_all_options( code, keypad ):
    options = [""]
    position = find_button_position( "A", keypad )
    for button in code:
        new_options = []
        target = find_button_position( button, keypad )
        for next_button in get_all_paths( position, target, keypad ):
            for option in options:
                new_options.append( option + next_button )
        options = new_options
        position = target
    return options

def do_path( code, keypad=REMOTE ):
    result = ""
    x, y = find_button_position( "A", keypad )
    for press in code:
        if press == ">":
            x += 1
        elif press == "<":
            x -= 1
        elif press == "v":
            y += 1
        elif press == "^":
            y -= 1
        if press == "A":
            result += keypad[ y ][ x ]
    return result

@lru_cache( 4096 )
def press_buttons_robots_in_between( buttons, robots ):
    if robots == 0:
        return len( buttons )
    else:
        pos = find_button_position( "A", REMOTE )
        result = 0
        for button in buttons:
            target = find_button_position( button, REMOTE )
            result += press_buttons_robots_in_between( get_shortest_path( pos, target ), robots - 1 )
            pos = target
        return result

def solve_star1():
    complexity = 0
    for code in read_file():
        robot_1 = calculate_presses( code, KEYPAD )
        robot_2 = calculate_presses( robot_1, REMOTE )
        fast = calculate_presses( robot_2, REMOTE )
        complexity += len( fast ) * int( code[:-1] )
    return complexity

def solve_star2():
    return sum( press_buttons_robots_in_between( calculate_presses( code, KEYPAD ), 25 )  * int( code[:-1] ) for code in read_file() )


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
