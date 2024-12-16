#! /usr/bin/python
import sys, getopt

def get_seating_values( data ):
    values = {}
    for line in data:
        parts = line[:-1].split()
        if parts[0] not in values:
            values[ parts[0]] = {}
        if parts[2] == "gain":
            values[ parts[0]][ parts[-1]] = int( parts[3])
        else:
            values[ parts[0]][ parts[-1]] = -int( parts[3])
    return values

def add_self( seating_values ):
    seating_values[ "Me" ] = {}
    for key in seating_values:
        seating_values[ "Me" ][ key ] = 0
        seating_values[ key ][ "Me" ] = 0
    return seating_values

def get_best_seating( values, people_to_place, last_before, first_after ):
    best = 0, []
    if len( people_to_place ) == 1:
        person = people_to_place[ 0 ]
        return values[ last_before ][ person ] + values[ person ][ last_before ] + values[ first_after ][ person ] + values[ person ][ first_after ], people_to_place
    for i, person in enumerate( people_to_place ):
        value, seating = get_best_seating( values, people_to_place[:i]+people_to_place[i+1:], person, first_after )
        score = values[ last_before ][ person ] + values[ person ][ last_before ] + value
        if score > best[0]:
            best = score, [person] + seating
    return best

def get_score( values, seating ):
    score = 0
    for i in range( len( seating ) ):
        score += values[ seating[ i ] ][ seating[ i-1 ] ]
        score += values[ seating[ i-1 ] ][ seating[ i ] ]
    return score

def solve_star1():
    values = get_seating_values( read_file() )
    people = [*values.keys()]

    best = 0
    for i, person in enumerate( people ):
        score, seating = get_best_seating( values, people[:i]+people[i+1:], person, person )
        if score > best:
            best = score
    return best

def solve_star2():
    values = add_self( get_seating_values( read_file() ) )
    people = [*values.keys()]

    best = 0
    for i, person in enumerate( people ):
        score, seating = get_best_seating( values, people[:i]+people[i+1:], person, person )
        if score > best:
            best = score
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
