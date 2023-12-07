#! /usr/bin/python
import sys, getopt

cards = "123456789TJQKA"

class Hand:
    def __init__(self, line, star=1):
        self.hand, bid = line.split()
        self.bid = int(bid)
        self.occurences = [ 0, 0, 0, 0, 0, 0 ]
        if star == 1:
            for card in cards:
                self.occurences[ 5-self.hand.count(card) ] += 1
        else:
            self.hand = self.hand.replace("J", "1")
            jokers = self.hand.count("1")
            for card in cards[1:]:
                self.occurences[ 5-self.hand.count(card) ] += 1
            i = 0
            while self.occurences[ i ] == 0:
                i += 1
            self.occurences[ i - jokers ] += 1
            self.occurences[ i ]-= 1



    def __eq__( self, other ):
        return self.hand == other.hand

    def __lt__( self, other ):
        for i in range( len( self.occurences ) ):
            if self.occurences[ i ] != other.occurences[ i ]:
                return self.occurences < other.occurences
        for i in range( len( self.hand ) ):
            if self.hand[ i ] != other.hand[ i ]:
                return cards.index(self.hand[ i ]) < cards.index(other.hand[i])
        return self.hand < other.hand

def solve_star1():
    hands = []
    for line in read_file():
        hands.append( Hand( line ) )
    result = 0
    for pos, hand in enumerate( sorted(hands) ):
        result += (pos+1)*hand.bid
    return result

def solve_star2():
    hands = []
    for line in read_file():
        hands.append( Hand( line, 2 ) )
    result = 0
    for pos, hand in enumerate( sorted(hands) ):
        result += (pos+1)*hand.bid
    return result


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
