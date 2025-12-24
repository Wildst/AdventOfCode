#! /usr/bin/python
import sys, getopt

class Node:
    def __init__(self, line, network):
        source, *destination = line.split()
        self.name = source.strip(":")
        self.connections = [*destination]
        self.routes_to_you = 0
        self.network = network
        network[self.name] = self

        self.paths = set()

    def add_connections_to_you(self, connection_count):
        self.routes_to_you += connection_count
        for nodeName in self.connections:
            if nodeName not in self.network:
                Node(nodeName, self.network)
            self.network[nodeName].add_connections_to_you(connection_count)

    def add_path(self, path):
        if self.name in path:
            return
        representation = str(sorted(path))
        if representation in self.paths:
            return
        self.paths.add(representation)
        longer_path = set(path)
        longer_path.add(self.name)

        for nodeName in self.connections:
            if nodeName not in self.network:
                Node(nodeName, self.network)
            self.network[nodeName].add_path(longer_path)

    def __repr__(self):
        return "Node: %s(%s): %s\n" % (self.name, self.routes_to_you, " ".join(self.connections))

    def get_connections(self, nodeName):
        return [path for path in self.paths if nodeName in path]



def solve_star1():
    network = {}
    for line in read_file():
        Node(line, network)

    if "out" not in network:
        Node("out", network)

    network["you"].add_connections_to_you(1)
    return network["out"].routes_to_you

def solve_star2():
    network = {}
    for line in read_file():
        Node(line, network)

    if "out" not in network:
        Node("out", network)

    network["svr"].add_path(set())
    connections = [connection for connection in network["out"].get_connections("svr") if "fft" in connection and "dac" in connection]
    return len(connections)


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
