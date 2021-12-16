#! /usr/bin/python3.8
import sys, getopt

def translate(hexadecimal):
    binary = ''
    for h in hexadecimal:
        binary += bin(int(h, 16))[2:].zfill(4)
    return binary

def new_packet(bits):
    packet = Packet()
    return packet.initiate(bits)


class Packet:
    def __init__(self):
        self.version = None
        self.type_id = None
        self.sub_packets = []
        self.value = -1

    def initiate(self, bits):
        self.version, bits = int(bits[:3], 2), bits[3:]
        self.type_id, bits = int(bits[:3], 2), bits[3:]
        if self.type_id == 4:
            return self.get_litaral_value(bits)
        else:
            return self.get_operator_value(bits)

    def get_litaral_value(self, bits):
        nr = ''
        while bits[0] == '1':
            nr, bits = nr+bits[1:5], bits[5:]
        nr, bits = nr+bits[1:5], bits[5:]
        self.value = int(nr, 2)
        return self, bits

    def get_operator_value(self, bits):
        if bits[0] == '1':
            amount, bits = int(bits[1:12], 2), bits[12:]
            for _ in range(amount):
                packet, bits = new_packet(bits)
                self.sub_packets.append(packet)
        else:
            amount, bits = int(bits[1:16], 2), bits[16:]
            sub_packets, bits = bits[:amount], bits[amount:]
            while '1' in sub_packets:
                packet, sub_packets = new_packet(sub_packets)
                self.sub_packets.append(packet)
        return self, bits

    def __repr__(self):
        return 'Packet:\n\tVersion: ' + str(self.version) + '\n\tType id: ' + str(self.type_id) + '\n\tValue: '+ str(self.value) + \
        ('\n\tSub packets: \n\t\t' + '\n\t\t'.join(['\n\t\t'.join(repr(packet).split('\n')) for packet in self.sub_packets]) if len(self.sub_packets) else '') + '\n'

    def get_version_sum(self):
        return self.version + sum(map(lambda p: p.get_version_sum(), self.sub_packets))

    def get_value(self):
        if self.type_id == 4:
            return self.value
        elif self.type_id == 0:
            return sum(map(lambda p: p.get_value(), self.sub_packets))
        elif self.type_id == 1:
            prod = 1
            for packet in self.sub_packets:
                prod *= packet.get_value()
            return prod
        elif self.type_id == 2:
            return min(map(lambda p: p.get_value(), self.sub_packets))
        elif self.type_id == 3:
            return max(map(lambda p: p.get_value(), self.sub_packets))
        elif self.type_id == 5:
            return 1 if self.sub_packets[0].get_value() > self.sub_packets[1].get_value() else 0
        elif self.type_id == 6:
            return 1 if self.sub_packets[0].get_value() < self.sub_packets[1].get_value() else 0
        elif self.type_id == 7:
            return 1 if self.sub_packets[0].get_value() == self.sub_packets[1].get_value() else 0



def solve_star1():
    bits = translate(read_file()[0])
    packet,_ = new_packet(bits)
    return packet.get_version_sum()


def solve_star2():
    bits = translate(read_file()[0])
    packet,_ = new_packet(bits)
    return packet.get_value()


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
