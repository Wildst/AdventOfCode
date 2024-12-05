#! /usr/bin/python
import sys, getopt

def parse_input( data ):
    rules = []
    books = []
    for line in data:
        pos = line.find("|")
        if pos > 0:
            rules.append( ( int( line[:pos] ), int( line[pos+1:] ) ) )
        elif line:
            books.append( [ *map( int,line.split(",") ) ] )
    return rules, books

def is_good( book, rules ):
    for first, second in rules:
        if first not in book or second not in book:
            continue
        if book.index( second ) < book.index( first ):
            return False
    return True

def get_correct_books( rules, books ):
    return [ book for book in books if is_good( book, rules ) ]

def get_bad_books( rules, books ):
    return [ book for book in books if not is_good( book, rules ) ]

def get_middle_page( book ):
    return book[ len( book ) // 2]

def solve_star1():
    rules, books = parse_input( read_file() )
    return sum( map( get_middle_page, get_correct_books( rules, books ) ) )

def fix_book( original_book, rules ):
    book = [ page for page in original_book ]
    changed = True
    while changed:
        changed = False
        for i in range( len( book ) ):
            for j in range( i+1, len( book ) ):
                if not is_good( [book[i],book[j]], rules ):
                    book[ i ], book[ j ] = book[ j ], book[ i ]
                    changed = True
    return book

def solve_star2():
    rules, books = parse_input( read_file () )
    return sum( get_middle_page( fix_book( book, rules ) ) for book in get_bad_books( rules, books ) )


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
