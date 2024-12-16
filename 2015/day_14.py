#! /usr/bin/python
import sys, getopt

class Reindeer:
    def __init__( self, line ):
        parts = line.split()
        self.name = parts[0]
        self.speed = int( parts[3] )
        self.stamina = int( parts[6] )
        self.recovery = int( parts[-2] )

    def get_distance( self, time ):
        remaining_time = time
        distance = 0
        while remaining_time > self.stamina:
            distance += self.stamina * self.speed
            remaining_time -= self.stamina + self.recovery
        if remaining_time > 0:
            distance += self.speed * remaining_time
        return distance

def solve_star1():
    all_reindeer = [ Reindeer( line ) for line in read_file() ]
    return max( reindeer.get_distance( 2503 ) for reindeer in all_reindeer )

def solve_star2():
    all_reindeer = [ Reindeer( line ) for line in read_file() ]
    scores = { reindeer.name: 0 for reindeer in all_reindeer }
    for i in range( 1, 2504 ):
        best_distance = max( reindeer.get_distance( i ) for reindeer in all_reindeer )
        for reindeer in all_reindeer:
            if reindeer.get_distance( i ) == best_distance:
                scores[ reindeer.name ] += 1
    return max( scores[ reindeer ] for reindeer in scores )


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
