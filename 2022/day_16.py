#! /usr/bin/python
import sys, getopt

class Cave:
    def __init__(self):
        self.valves = {}
        self.bests = [{} for _ in range(30)]
        self.max_valves = 0
        self.useful_valves = []
        self.distances = {}

    def add_valve(self, line):
        _, valve, _, _, rate, _, _, _, _, *destinations = line.split()
        rate = int(rate[5:-1])
        if rate:
            self.max_valves += 1
            self.useful_valves.append( valve )
        self.valves[valve] = (rate, set([destination.strip(",") for destination in destinations]))

    def find_shortest_path( self, valve1, valve2 ):
        nodes = set( self.valves.keys() )
        distances = { k: 100 for k in nodes }
        distances[ valve1 ] = 0
        nodes_to_check = [ v for v in self.valves[ valve1 ][ 1 ] ]
        nodes.remove( valve1 )
        while nodes_to_check:
            node = nodes_to_check[0]
            nodes_to_check = nodes_to_check[ 1:]
            found_option = False
            for neighbour in self.valves[ node ][1]:
                if distances[ neighbour ]+ 1 < distances[ node ]:
                    distances[ node ] = distances[ neighbour ] + 1
                    found_option = True
            if found_option:
                for neighbour in self.valves[ node ][ 1 ]:
                    if neighbour not in nodes_to_check:
                        nodes_to_check.append( neighbour )
        return distances[ valve2 ]



    def calculate_distances(self):
        for valve in self.useful_valves:
            self.distances[ valve ] = {}
            for other_valve in self.useful_valves:
                if valve != other_valve:
                    self.distances[ valve ][ other_valve ] = self.find_shortest_path( valve, other_valve )


    def release_max_pressure(self, start_valve, open_valves, time_left):
        hashable_open_valves = "".join(sorted(open_valves))

        if time_left == 0:
            return 0

        if start_valve not in self.bests[30-time_left]:
            self.bests[30-time_left][start_valve] = {}

        if hashable_open_valves in self.bests[30-time_left][start_valve]:
            return self.bests[30-time_left][start_valve][hashable_open_valves]

        if len( open_valves) == len(self.valves):
            self.bests[30-time_left][start_valve][hashable_open_valves] = 0
            return 0

        for i in range( 30-time_left):
            if start_valve in self.bests[i] and hashable_open_valves in self.bests[i][start_valve]:
                return 0

        best = 0
        if self.valves[start_valve][0] and start_valve not in open_valves:
            test_valves = open_valves.copy()
            test_valves.append(start_valve)
            test = self.release_max_pressure(start_valve, test_valves, time_left-1)
            best = (time_left-1)*self.valves[start_valve][0] + test
        for valve in self.valves[start_valve][1]:
            test = self.release_max_pressure(valve, open_valves, time_left-1)
            if test > best:
                best = test

        self.bests[30-time_left][start_valve][hashable_open_valves] = best
        return best

    def release_max_pressure_helped(self, my_valve, elephant_valve, open_valves, time_left, travel_times ):
        hashable_open_valves = ",".join(sorted(open_valves))

        if my_valve < elephant_valve:
            my_valve, elephant_valve = elephant_valve, my_valve

        if time_left == 0:
            return 0

        if (my_valve, elephant_valve) not in self.bests[26-time_left]:
            self.bests[26-time_left][(my_valve, elephant_valve)] = {}

        if len( open_valves) == self.max_valves:
            self.bests[26-time_left][(my_valve, elephant_valve)][hashable_open_valves] = 0
            return 0

        self.bests[26-time_left][(my_valve, elephant_valve)][hashable_open_valves] = 0

        if time_left >= 10:
            print(my_valve, elephant_valve, open_valves, time_left)

        if travel_times[0] == 0:
            # open own valve
            if my_valve not in open_valves:
                

        # do not open own valve
        for new_valve in self.valves[my_valve][1]:
            if self.valves[elephant_valve] and elephant_valve not in open_valves:
                test_valves = open_valves.copy()
                test_valves.append(elephant_valve)
                test = self.release_max_pressure_helped(new_valve, elephant_valve, test_valves, time_left-1)
                test += (time_left-1)*self.valves[elephant_valve][0]
                best = max(test, best)
            for test_valve in self.valves[elephant_valve][1]:
                best = max(best, self.release_max_pressure_helped(new_valve, test_valve, open_valves, time_left-1))

        self.bests[26-time_left][(my_valve, elephant_valve)][hashable_open_valves] = best
        return best


def solve_star1():
    cave = Cave()
    for line in read_file():
        cave.add_valve(line)
    return cave.release_max_pressure('AA', [], 30)

def solve_star2():
    cave = Cave()
    for line in read_file():
        cave.add_valve(line)
    cave.calculate_distances()
    print( cave.distances )
    return cave.release_max_pressure_helped('AA', 'AA', [], 26, [0,0])

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
