#! /usr/bin/python
import sys, getopt

def solve_star1():
    start_time, lines = read_file()
    start_time = int(start_time)
    lines = [int(line) for line in lines.split(",") if line != "x"]
    time = start_time
    test = [line for line in lines if time % line == 0]
    while not test:
        time += 1
        test = [line for line in lines if time % line == 0]
    print((time - start_time) * test[0])



def solve_star2():
    _, lines = read_file()
    lines = [int(line) if line != "x" else 1 for line in lines.split(",")]
    repetition_rate = 1
    timestamp = 0
    for offset, line in enumerate(lines):
        # get earliest timestamp
        while (offset + timestamp) %line != 0:
            timestamp += repetition_rate
        # check repetition rate
        test_time = timestamp + repetition_rate
        while (offset + test_time) % line != 0:
            test_time += repetition_rate
        repetition_rate = test_time - timestamp

    print(timestamp)


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
        solve_star1()
    elif star == 2:
        solve_star2()









