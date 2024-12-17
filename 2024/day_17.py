#! /usr/bin/python
import sys, getopt

class Computer:
    def __init__(self, registers, program ):
        self.A, self.B, self.C = registers
        self.program = program

        self.ip = 0
        self.output = []


    def get_combo_operand( self, combo_operand ):
        if combo_operand == 4:
            return self.A
        elif combo_operand == 5:
            return self.B
        elif combo_operand == 6:
            return self.C
        elif combo_operand == 7:
            print( "Invalid" )
            return -1
        else:
            return combo_operand

    def do_instruction( self ):
        opcode = self.program[ self.ip ]
        operand = self.program[ self.ip + 1 ]
        self.ip += 2
        if opcode == 0: # adv
            self.A = self.A // ( 2**self.get_combo_operand( operand ) )
        elif opcode == 1: # bxl
            self.B = self.B ^ operand
        elif opcode == 2: # bst
            self.B = self.get_combo_operand( operand ) % 8
        elif opcode == 3: # jnz
            if self.A != 0:
                self.ip = operand
        elif opcode == 4: # bxc
            self.B = self.B ^ self. C
        elif opcode == 5: # out
            self.output.append( self.get_combo_operand( operand ) % 8 )
        elif opcode == 6: # bdv
            self.B = self.A // ( 2**self.get_combo_operand( operand ) )
        elif opcode == 7: # cdv
            self.C = self.A // ( 2**self.get_combo_operand( operand ) )

    def run( self ):
        while self.ip < len( self.program ):
            self.do_instruction()
        return self.output


def solve_star1():
    data = read_file()
    registers = [ int( data[ i ].split()[-1] ) for i in range( 3 ) ]
    program = [ int( value ) for value in data[ -1 ].split()[-1].split(",") ]
    computer = Computer( registers, program )

    return ",".join( map( str, computer.run() ) )

def solve_star2():
    data = read_file()
    registers = [ int( data[ i ].split()[-1] ) for i in range( 3 ) ]
    program = [ int( value ) for value in data[ -1 ].split()[-1].split(",") ]

    last_options = [0]
    for i in range( len( program ) ):
        options = []
        for j in range( 8 ):
            for option in last_options:
                test = option << 3
                test += j
                registers[ 0 ] = test
                if Computer( registers, program ).run()[0] == program[-i-1 ]:
                    options.append( test )
        last_options = options
    return min( options )

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
