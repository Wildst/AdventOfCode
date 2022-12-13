#! /usr/bin/python
import sys, getopt

def parse_list(input):
    result = []
    while not input.startswith("]"):
        if input.startswith('['):
            item, input = parse_list(input[1:])
            result.append(item)
        elif( input.startswith(',') ):
            input = input[1:]
        else:
            item, *rest = input.split(',')
            if not rest:
                rest = [""]
            while item[-1] == ']':
                item = item[:-1]
                rest[0] = ']' + rest[0]

            result.append(int(item))
            input = ",".join(rest)
    return result, input[1:]

def compare(left, right):
    if type(left) == list:
        if type(right) == list:
            if not left:
                return len(right)
            if not right:
                return -1
            check = compare(left[0], right[0])
            if check != 0:
                return check
            else:
                return compare(left[1:], right[1:])
        return compare(left, [right])
    if type(right) == list:
        return compare([left], right)
    return right - left

def right_order(left, right):
    return compare(left, right) > 0

def solve_star1():
    lines = read_file()
    result = 0
    for i in range(0,len(lines),3):
        line_1 = parse_list(lines[i][1:])[0]
        line_2 = parse_list(lines[i+1][1:])[0]
        if right_order(line_1, line_2):
            result += 1 + i // 3
    return result

def insert_packet(packets, packet):
    i = 0
    while i < len(packets) and right_order(packets[i], packet):
        i += 1
    packets.insert(i, packet)
    return packets, i + 1

def solve_star2():
    packets = []
    for line in read_file():
        if line:
            packets, _ = insert_packet(packets, parse_list(line[1:])[0])
    packets, pos1 = insert_packet(packets, [[2]])
    packets, pos2 = insert_packet(packets, [[6]])
    return pos1*pos2




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
