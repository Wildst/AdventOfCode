#! /usr/bin/python
import sys, getopt

def print_rocks(rocks, origin, sand):
    minx = min( origin[0], min(r[0] for r in rocks), min(r[0] for r in sand) if sand else origin[0])
    maxx = max( origin[0], max(r[0] for r in rocks), max(r[0] for r in sand) if sand else origin[0])
    maxy = max( origin[1], max(r[1] for r in rocks), max(r[1] for r in sand) if sand else origin[1])
    field = [["." for _ in range(maxx-minx+1)] for _ in range(maxy+1)]

    for x,y in rocks:
        field[y][x-minx] = "#"
    field[origin[1]][origin[0]-minx] = '+'
    for x,y in sand:
        field[y][x-minx] = "o"
    [print("".join(line)) for line in field]

def can_fall(sand, rock, set_sand):
    return fall(sand, rock,set_sand) != sand

def fall(sand, rock, set_sand):
    x,y = sand
    if (x, y+1) not in rock and (x, y+1) not in set_sand:
        return (x, y+1)
    if (x-1, y+1) not in rock and (x-1, y+1) not in set_sand:
        return (x-1, y+1)
    if (x+1, y+1) not in rock and (x+1, y+1) not in set_sand:
        return (x+1, y+1)
    return x, y


def solve_star1():
    rock = set()
    for line in read_file():
        parts = line.split()
        location = [*map(int, parts[0].split(','))]
        for i in range(2, len(parts), 2):
            destination = [*map(int, parts[i].split(','))]
            if destination[0] == location[0]:
                y1, y2 = sorted([destination[1], location[1]])
                for y in range(y1, y2+1):
                    rock.add((destination[0], y))
            else:
                x1, x2 = sorted([destination[0], location[0]])
                for x in range(x1, x2+1):
                    rock.add((x, destination[1]))
            location = destination
    stacking = True
    set_sand = set()
    origin = (500,0)

    maxy = max( origin[1], max(r[1] for r in rock))

    while stacking:
        sand = origin
        while can_fall(sand, rock, set_sand) and sand[1] <= maxy:
            sand = fall(sand, rock, set_sand)
        if sand[1] <= maxy:
            set_sand.add(sand)
        else:
            stacking = False

    print_rocks(rock, origin, set_sand)

    return len(set_sand)

def solve_star2():
    rock = set()
    for line in read_file():
        parts = line.split()
        location = [*map(int, parts[0].split(','))]
        for i in range(2, len(parts), 2):
            destination = [*map(int, parts[i].split(','))]
            if destination[0] == location[0]:
                y1, y2 = sorted([destination[1], location[1]])
                for y in range(y1, y2+1):
                    rock.add((destination[0], y))
            else:
                x1, x2 = sorted([destination[0], location[0]])
                for x in range(x1, x2+1):
                    rock.add((x, destination[1]))
            location = destination
    stacking = True
    set_sand = set()
    origin = (500,0)

    maxy = max( origin[1], max(r[1] for r in rock))

    while stacking:
        sand = origin
        while can_fall(sand, rock, set_sand) and sand[1] <= maxy:
            sand = fall(sand, rock, set_sand)
        if sand in set_sand:
            stacking = False
        set_sand.add(sand)


    print_rocks(rock, origin, set_sand)

    return len(set_sand)


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
