#! /usr/bin/python
import sys, getopt

class Directory:
    def __init__(self, name):
        self.subdirectories = {}
        self.files = []
        self.size = -1
        self.parent = None
        self.name = name

    def add_subdirectory(self, name, directory):
        self.subdirectories[name] = directory
        directory.set_parent(self)

    def set_parent(self, directory):
        if not self.parent:
            self.parent = directory

    def get_size(self):
        if self.size < 0:
            self.size = sum(s for s,n in self.files)
            self.size += sum( self.subdirectories[name].get_size() for name in self.subdirectories)
        return self.size

    def print(self, depth):
        result = "  "*depth + "- " + self.name + "\n"
        for name in self.subdirectories.keys():
            result += self.subdirectories[name].print(depth + 1)
        for size, name in self.files:
            result += "  "*depth + "- " +name + " (" + str(size) + ")\n"
        return result

    def __str__(self):
        return self.print(0)

    def __repr__(self):
        return str(self)

def parse_directories():
    root = Directory("/")
    current_directory = root
    all_directories = [root]
    for line in read_file():
        if line.startswith('$'):
            if "cd" in line:
                target_directory = line.split()[-1]
                if target_directory == '/':
                    current_directory = root
                elif target_directory == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.subdirectories[target_directory]
        elif line.startswith("dir"):
            all_directories.append(Directory(line.split()[-1]))
            current_directory.add_subdirectory(line.split()[-1], all_directories[-1])
        else:
            size, name = line.split()
            current_directory.files.append((int(size), name))
    return all_directories


def solve_star1():
    return sum( directory.get_size() for directory in parse_directories() if directory.get_size() < 100000)


def solve_star2():
    total_space = 70000000
    needed_space = 30000000
    directories = parse_directories()
    free_space = total_space - directories[0].get_size()
    needed_space -= free_space

    best = directories[0]
    for directory in directories:
        if needed_space <= directory.get_size() < best.get_size():
            best = directory
    return best.get_size()


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
