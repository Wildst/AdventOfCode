#! /usr/bin/python
import sys, getopt

HIGH = True
LOW = False

OFF = False
ON = True

class Module:
    def __init__( self, name ):
        self.name = name
        self.outputs = []
        self.inputs = []
        self.variant = ""
        self.high_pulses_received = 0
        self.low_pulses_received = 0

    def set_variant( self, variant ):
        self.variant = variant
        if self.variant == "%":
            self.state = OFF
        if self.variant == "&":
            self.state = { module: LOW for module in self.inputs }

    def add_output( self, output ):
        self.outputs.append( output )

    def add_input( self, input ):
        self.inputs.append( input.name )
        if self.variant == "&":
            self.state[ input.name ] = LOW

    def receive_pulse( self, origin, pulse ):
        if pulse == HIGH:
            self.high_pulses_received += 1
        else:
            self.low_pulses_received += 1
        if self.variant == "%":
            if pulse == LOW:
                self.state = not self.state
                return True, self.state
        elif self.variant == "&":
            self.state[ origin.name ] = pulse
            if all( state == HIGH for state in self.state.values() ):
                return True, LOW
            else:
                return True, HIGH
        else:
            return True, pulse
        return False, pulse

    def __repr__( self ):
        state = ""
        if self.variant == "%":
            state = "on" if self.state else "off"
        elif self.variant == "&":
            state = ", ".join( "%s: %s" % ( module, self.state[ module ] ) for module in self.state.keys() )
        return "%s%s -> %s\n\t%s" % (self.variant, self.name, ", ".join( output.name for output in self.outputs ), state )

def parse_modules( lines ):
    modules = {}
    for line in lines:
        module, outputs = line.split("->")
        name = module.strip()
        variant = ""
        if name[0] in "%&":
            variant = name[ 0 ]
            name = name[1:]
        if name not in modules.keys():
            modules[ name ] = Module( name )
        if variant:
            modules[ name ].set_variant( variant )
        for output in outputs.split(","):
            output_name = output.strip()
            if output_name not in modules.keys():
                modules[ output_name ] = Module( output_name )
            modules[ output_name ].add_input( modules[ name ] )
            modules[ name ].add_output( modules[ output_name ] )

    modules["button"] = Module( "button" )
    modules["button"].add_output( modules["broadcaster"])
    return modules

def press_button( modules ):
    pulses = []
    pulses.append( ( "button", LOW ) )
    while pulses:
        module, pulse = pulses[ 0 ]
        pulses = pulses[1:]
        module = modules[ module ]
        for output in module.outputs:
            # print( "%s -%s-> %s" %( module.name, "low" if pulse == LOW else "high", output.name ) )
            state, next_pulse = output.receive_pulse( module, pulse )
            if state:
                pulses.append( ( output.name, next_pulse ) )
    return modules


def solve_star1():
    modules = parse_modules( read_file() )
    for _ in range( 1000 ):
        modules = press_button( modules )
        # print()
    return sum( module.low_pulses_received for module in modules.values() ) * sum( module.high_pulses_received for module in modules.values() )

def solve_star2():
    modules = parse_modules( read_file() )
    if not "rx" in modules.keys():
        return "No module 'rx' found."
    count = 0
    parts = { module.name : 0 for module in modules[ "rx" ].inputs }
    while modules[ "rx" ].low_pulses_received == 0:
        modules = press_button( modules )
        count += 1
        if count % 1000000 == 0:
            print( count )
    return count


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
