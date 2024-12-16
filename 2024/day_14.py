#! /usr/bin/python
import sys, getopt

class Robot:
    def __init__( self, line ):
        p,v = line.split()
        p_parts = p[2:].split(",")
        v_parts = v[2:].split(",")
        self.position = int(p_parts[0]), int(p_parts[1])
        self.velocity = int(v_parts[0]), int(v_parts[1])

    def __repr__( self ):
        return "\nRobot: p=%i,%i v=%i,%i" % (self.position[0], self.position[1], self.velocity[0], self.velocity[1])

    def do_move( self, amount ):
        self.position = (self.position[0] + self.velocity[0]*amount)%size[0], (self.position[1] + self.velocity[1]*amount)%size[1]


def solve_star1():
    robots = [ Robot( line ) for line in read_file() ]
    for robot in robots:
        robot.do_move( 100 )
    quadrants = [0,0,0,0]
    for robot in robots:
        if robot.position[0] < size[0] // 2:
            if robot.position[1] < size[1] // 2:
                quadrants[0]+=1
            elif robot.position[1] > size[1] // 2:
                quadrants[1]+=1
        if robot.position[0] > size[0] // 2:
            if robot.position[1] < size[1] // 2:
                quadrants[2]+=1
            elif robot.position[1] > size[1] // 2:
                quadrants[3]+=1
    result = 1
    for quadrant in quadrants:
        result *= quadrant
    return result

def display(robots):
    s = [[" " for _ in range(size[0])] for _ in range(size[1])]
    for robot in robots:
        x,y = robot.position
        s[y][x] = "#"
    for line in s:
        print( "".join( line ) )

def could_be_tree( robots ):
    counts = [0]*size[1]
    positions = set( robot.position for robot in robots )
    for robot in robots:
        x,y = robot.position
        if (x-1,y+1) in positions and (x+1,y+1) in positions and (x-2,y+2) in positions and (x+2,y+2) in positions and (x-3,y+3) in positions and (x+3,y+3) in positions:
            return True

    return False


def solve_star2():
    robots = [ Robot( line ) for line in read_file() ]
    display(robots)
    i = 0
    while True:
        i += 1
        for robot in robots:
            robot.do_move( 1 )
        if could_be_tree( robots ):
            display(robots)
            print( i )
            input()
    return ""


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][0:-2] + "in"
    file_dir = "input_files"
    size = (101,103)
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
            size = (11,7)

    if star == 1:
        print(solve_star1())
    elif star == 2:
        print(solve_star2())
