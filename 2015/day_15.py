#! /usr/bin/python
import sys, getopt

def get_value( amounts, ingredients ):
    properties = [ 0 for _ in range( 4 ) ]
    for i, ingredient in enumerate( ingredients ):
        for j in range( 4 ):
            properties[ j ] += ingredient[ j ] * amounts[ i ]
    result = 1
    for property in properties:
        result *= max( property, 0 )
    if result == 0:
        result = sum( [ property for property in properties if property > 0 ] ) * sum( [ property for property in properties if property < 0 ] )
    return result

def get_swaps( ingredient, amounts ):
    options = []
    amounts = [ v for v in amounts ]
    amounts[ ingredient ] -= 1
    for i in range( len( amounts ) ):
        if i != ingredient:
            option = [ v if j != i else v+1 for j, v in enumerate( amounts ) ]
            if min( option ) >= 0:
                options.append( option )
    return options

def solve_star1():
    ingredients = [ [ int( part.strip( "," ) ) for part in line.split()[ 2::2 ] ] for line in read_file() ]
    amounts = [ 100 // len( ingredients ) //2 for _ in ingredients ]
    amounts[ 0 ] += 100 - sum( amounts )

    todo = set()
    todo.add( 0 )
    best = -99999999999999999999999999
    while todo:
        ingredient = todo.pop()
        for swap in get_swaps( ingredient, amounts ):
            value = get_value( swap, ingredients )
            if value > best:
                best = value
                for i in range( len( swap ) ):
                    if swap[ i ] != amounts[ i ]:
                        todo.add( i )
                amounts = swap
            print( amounts, value, swap )

    print( amounts )
    return best

def generate_calories_cookies( ingredients, calories, space ):
    if len( ingredients ) == 1:
        if ingredients[ 0 ][ -1 ] * space == calories:
            return [ [ space ] ]
        else:
            return []

    options = []
    i = 0
    while i < space and ingredients[ 0 ][ -1 ] * i < calories:
        for option in generate_calories_cookies( ingredients[1:], calories - ingredients[0][-1]*i, space - i ):
            options.append( [ i ] + option )
        i += 1
    return options

def solve_star2():
    ingredients = [ [ int( part.strip( "," ) ) for part in line.split()[ 2::2 ] ] for line in read_file() ]
    options = generate_calories_cookies( ingredients, 500, 100 )

    return max( get_value( option, ingredients ) for option in options )


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
