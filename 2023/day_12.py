#! /usr/bin/python
import sys, getopt
from functools import lru_cache

def can_be_start( records, size ):
    for i in range( size ):
        if records[ i ] == ".":
            return False
    return len( records ) <= size or records[ size ] != "#"


def count_arangements( records, groups ):
    @lru_cache
    def count_internal( record_pos, group_pos ):
        if group_pos == len( groups ):
            return 1 if not "#" in records[record_pos:] else 0
        if len(records[record_pos:]) < sum( groups[group_pos:] ) + len( groups[group_pos:] ) - 1:
            return 0
        count = 0
        if records[record_pos] != "#":
            count += count_internal( record_pos + 1, group_pos )
        if can_be_start( records[record_pos:], groups[ group_pos ] ):
            count += count_internal( record_pos + 1+groups[group_pos], group_pos + 1)
        return count
    return count_internal( 0, 0 )

def solve_star1():
    total = 0
    for line in read_file():
        records, groups = line.split()
        groups = [ *map( int, groups.split(",")) ]
        arrangements = count_arangements( records, groups )
        total += arrangements
        print( records, groups, arrangements )
    return total

def solve_star2():
    total = 0
    for line in read_file():
        records, groups = line.split()
        groups = [ *map( int, ",".join(groups for _ in range( 5 )).split(",")) ]
        records = "?".join( [records for _ in range( 5 )])

        arrangements = count_arangements( records, groups )
        total += arrangements
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
