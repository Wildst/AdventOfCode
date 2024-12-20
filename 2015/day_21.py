#! /usr/bin/python
import sys, getopt


WEAPONS = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

ARMOR = """Armor:      Cost  Damage  Armor
None          0     0       0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""

RINGS = """Rings:      Cost  Damage  Armor
None          0     0       0
None          0     0       0
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""


class Item:
    def __init__( self, line ):
        parts = line.split()
        self.name = " ".join( parts[ :-3 ] )
        self.cost = int( parts[ -3 ] )
        self.damage = int( parts[ -2 ] )
        self.armor = int( parts[ -1 ] )

    def __repr__( self ):
        return "Item:\n\tName: %s\n\tCost: %i\n\tDamage: %i\n\tArmor: %i\n" % ( self.name, self.cost, self.damage, self.armor )

class Fighter:
    def __init__( self ):
        self.max_hp = 100
        self.hp = self.max_hp
        self.damage = 0
        self.armor = 0

    def equip_item( self, item ):
        self.damage += item.damage
        self.armor += item.armor

    def prepare( self, items=[] ):
        self.hp = self.max_hp
        if items:
            self.damage = 0
            self.armor = 0
            for item in items:
                self.equip_item( item )

    def is_alive( self ):
        return self.hp > 0

    def hit( self, other ):
        other.hp -= max( self.damage - other.armor, 1 )

def parse_boss( data ):
    boss = Fighter()
    boss.max_hp = int( data[0].split()[-1] )
    boss.damage = int( data[1].split()[-1] )
    boss.armor = int( data[2].split()[-1] )
    return boss

def fight( player, boss ):
    while player.is_alive() and boss.is_alive():
        player.hit( boss )
        boss.hit( player )
    return not boss.is_alive()

def calc_cost( items ):
    return sum( item.cost for item in items )

def get_equipment_options():
    weapons = [ Item( weapon ) for weapon in WEAPONS.splitlines()[1:] ]
    armor = [ Item( armor ) for armor in ARMOR.splitlines()[1:] ]
    rings = [ Item( ring ) for ring in RINGS.splitlines()[1:] ]
    options = []
    for weapon in weapons:
        for armor_option in armor:
            for i, ring1 in enumerate( rings ):
                for ring2 in rings[i+1:]:
                    options.append( [weapon, armor_option, ring1, ring2 ] )
    return sorted( options, key=calc_cost )

def solve_star1():
    boss = parse_boss( read_file() )
    player = Fighter()

    for gear in get_equipment_options():
        boss.prepare()
        player.prepare( gear )
        if fight( player, boss ):
            print( gear )
            return calc_cost( gear )
    return -1


def solve_star2():
    boss = parse_boss( read_file() )
    player = Fighter()

    for gear in get_equipment_options()[::-1]:
        boss.prepare()
        player.prepare( gear )
        if not fight( player, boss ):
            print( gear )
            return calc_cost( gear )
    return -1


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
