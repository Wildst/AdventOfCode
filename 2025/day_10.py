#! /usr/bin/python
import sys, getopt

def critical_light(buttons):
    light_count = max(map(max,buttons))
    counts = [len(button for button in buttons if light in button) for light in range(light_count)]
    return counts

class Machine:
    def __init__(self, line):
        target, *schematics, requirements = line.split()
        self.original = target
        self.target = int( "".join(["1" if s == "#" else "0" for s in target[1:-1]]), 2)
        self.light_count = len(target) - 2
        self.buttons = [set(map(int, b[1:-1].split(","))) for b in schematics]
        self.joltages = tuple(map(int, requirements[1:-1].split(",")))

    def find_best_lights(self, remaining_buttons, lights = 0):
        if lights == self.target:
            return 0
        if not remaining_buttons:
            return 1000
        without_press = self.find_best_lights(remaining_buttons[1:], lights)
        after_press = lights
        for button in remaining_buttons[0]:
            after_press ^= 1 << (self.light_count - button-1)
        with_press = self.find_best_lights(remaining_buttons[1:], after_press) + 1
        return min(without_press, with_press)

    def find_best_joltages(self, options):
        if self.joltages in options:
            return 0
        new_options = set()
        for button in self.buttons:
            for option in options:
                new_option = tuple( v + 1 if i in button else v for i, v in enumerate(option))
                good = True
                for i, current in enumerate(new_option):
                    if current > self.joltages[i]:
                        good = False
                        break
                if good:
                    new_options.add(new_option)
        return self.find_best_joltages(new_options) + 1

    def __repr__(self):
        target = ""
        for i in range(self.light_count-1, -1, -1):
            if 1 << i & self.target:
                target += "#"
            else:
                target += "."
        return "Machine:\n\tTarget: \t%s\n\tButtons: \t%s\n\tjoltages: \t%s\n" % (target, self.buttons, self.joltages)

def solve_star1():
    machines = [Machine(line) for line in read_file()]
    return sum( machine.find_best_lights(machine.buttons) for machine in machines)

def solve_star2():
    machines = [Machine(line) for line in read_file()]
    result = 0
    for machine in machines:
        s = set()
        s.add(tuple(0 for _ in range(machine.light_count)))
        best = machine.find_best_joltages(s)
        print(machine, best)
        result += best
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
