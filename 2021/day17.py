#! /usr/bin/python3.8
import sys, getopt

def solve_star1():
    min_y, max_y = sorted(map(int, read_file()[0].split('=')[-1].split('..')))
    best_height = 0
    for i in range(abs(min_y)):
        height = 0
        velocity = i
        max_height = 0
        while height > max_y:
            height += velocity
            velocity -= 1
            max_height = max(height, max_height)

        if height >= min_y and max_height > best_height:
            best_height = max_height
    return best_height

def solve_star2():
    x,y = read_file()[0].split('=')[1:]
    min_x, max_x = sorted(map(int, x.split(',')[0].split('..')))
    min_y, max_y = sorted(map(int, y.split('..')))
    pos = set()
    for x in range(max_x+1):
        for y in range(min_y, abs(min_y)):
            x_pos, y_pos = 0, 0
            x_velocity, y_velocity = x, y
            while y_pos >= min_y and x <= max_x:
                x_pos, y_pos = x_pos + x_velocity, y_pos + y_velocity
                if x_velocity > 0:
                    x_velocity -= 1
                y_velocity -= 1

                if max_y >= y_pos >= min_y and min_x <= x_pos <= max_x:
                    pos.add((x, y))


    return len(pos)


def read_file():
    with open(file_dir + "/" + infile) as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    infile = sys.argv[0][2:-2] + "in"
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
