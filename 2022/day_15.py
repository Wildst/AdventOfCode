#! /usr/bin/python
import sys, getopt

def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def covered( location, sensors, beacons ):
    return not location in beacons and [s for s, d in sensors if 0 <= distance(s, location)<=d]

def solve_star1():
    sensors = []
    beacons = set()
    for line in read_file():
        parts = line.split()
        sensor = int(parts[2].split('=')[1][:-1]), int(parts[3].split('=')[1][:-1])
        beacon = int(parts[-2].split('=')[1][:-1]), int(parts[-1].split('=')[1])
        beacons.add(beacon)
        sensors.append((sensor, distance(sensor, beacon)))
    minx = min( sensor[0]-d for sensor, d in sensors)
    maxx = max( sensor[0]+d for sensor, d in sensors)
    y = 2000000
    return len([x for x in range(minx, maxx+1) if covered((x,y), sensors, beacons)])


def solve_star2():
    sensors = []
    beacons = set()
    for line in read_file():
        parts = line.split()
        sensor = int(parts[2].split('=')[1][:-1]), int(parts[3].split('=')[1][:-1])
        beacon = int(parts[-2].split('=')[1][:-1]), int(parts[-1].split('=')[1])
        beacons.add(beacon)
        sensors.append((sensor, distance(sensor, beacon)))
    m = 4000000
    sol = 0
    y = 0
    while y <= m:
        x = 0
        while x <= m:
            if not covered((x,y), sensors, beacons):
                print(x,y)
                sol = 4000000*x+y
            for sensor, d in sensors:
                xs, ys = sensor
                xdiff = abs(x-xs)
                ydiff = abs(y-ys)
                if xdiff <= d-ydiff:
                    x = max(x, xs+d-ydiff)
            x += 1
        y += 1
        if not y % 40000:
            print(y//40000)
    return sol


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
