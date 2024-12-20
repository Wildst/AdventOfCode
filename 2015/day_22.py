#! /usr/bin/python
import sys, getopt
from copy import deepcopy

SPELLS = { "Magic Missile": 53, "Drain": 73, "Shield": 113, "Poison": 173, "Recharge": 229 }

class Player:
    def __init__( self ):
        self.hp = 50
        self.damage = 8
        self.mana = 500
        self.default_armor = 0
        self.armor = self.default_armor
        self.poisoned = 0
        self.shielded = 0
        self.recharging = 0

    def attack( self, other ):
        other.hp -= max( self.damage - other.armor, 1 )

    def is_alive( self ):
        return self.hp > 0 and self.mana > 0

    def apply_effects( self ):
        if self.poisoned:
            self.hp -= 3
            self.poisoned -= 1
        self.armor = 0
        if self.shielded:
            self.armor += 7
            self.shielded -= 1
        if self.recharging:
            self.mana += 101
            self.recharging -= 1

    def cast_spell( self, spell, target ):
        self.mana -= SPELLS[ spell ]
        if spell == "Magic Missile":
            target.hp -= 4
        elif spell == "Drain":
            target.hp -= 2
            self.hp += 2
        elif spell == "Shield":
            if self.shielded:
                return False
            self.shielded = 6
        elif spell == "Poison":
            if target.poisoned:
                return False
            target.poisoned = 6
        elif spell == "Recharge":
            if self.recharging:
                return False
            self.recharging = 5
        else:
            print( "Unknown spell:", spell )
        return True

def find_min_mana( player: Player, boss: Player, spell="", best = 9999999999999999999999999999999999999999999999999999999999999, cast_spells = [], hard_mode = False ):
    if spell and best <= SPELLS[ spell ]:
        return -1
    mana_spend = 0
    if spell:
        if hard_mode:
            player.hp -= 1
            if not player.is_alive():
                return -1
        player.apply_effects()
        boss.apply_effects()
        if not boss.is_alive():
            return mana_spend
        if not player.cast_spell( spell, boss ) or not player.is_alive():
            return -1
        mana_spend += SPELLS[ spell ]
        player.apply_effects()
        boss.apply_effects()
        if not boss.is_alive():
            return mana_spend
        boss.attack( player )
    if mana_spend > best:
        return -1
    if not boss.is_alive():
        return mana_spend
    if not player.is_alive():
        return -1

    can_win = False
    for next_spell in SPELLS:
        player_state = deepcopy( player )
        boss_state = deepcopy( boss )
        test = find_min_mana( player_state, boss_state, next_spell, best - mana_spend, cast_spells + [ spell ], hard_mode )
        if 0 <= test < best and test:
            best = test
            can_win = True
    if can_win:
        return best + mana_spend
    return -1

def create_boss( data ):
    boss = Player()
    boss.hp = int( data[0].split()[-1] )
    boss.damage = int( data[1].split()[-1] )
    return boss

def solve_star1():
    player = Player()
    boss = create_boss( read_file() )
    return find_min_mana( player, boss )

def solve_star2():
    player = Player()
    boss = create_boss( read_file() )
    return find_min_mana( player, boss, hard_mode=True )


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
