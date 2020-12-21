#! /usr/bin/python
import sys, getopt
from functools import reduce
UNKNOWN = "unknown risks"

class Allergen():
    def __init__(self, name, food_options):
        self.name = name
        self.food = set(food_options)

    def found_origin(self):
        if isinstance(self.food, str):
            return self.food
        return False

    def check_origin(self):
        if not self.found_origin() and len(self.food) == 1:
            self.food = self.food.pop()
            return self.food

        return False

    def remove(self, food):
        if not self.found_origin() and food in self.food:
            self.food.remove(food)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        if self.found_origin():
            return self.name + " found in " + self.food
        return self.name + " found in " + " or ".join(self.food) + "."

    def __repr__(self):
        return str(self)

class Food():
    def __init__(self, name):
        self.name = name
        self.amounts_used = 1
        self.allergen = UNKNOWN

    def __eq__(self, other):
        return self.name == other.name

    def is_used(self):
        self.amounts_used += 1


def solve_star1():
    all_foods = {}
    all_allergens = {}
    for line in read_file():
        recipe_foods, allergens = line[:-1].split(" (contains ")
        recipe_foods = recipe_foods.split(" ")
        for food in recipe_foods:
            if food not in all_foods:
                all_foods[food] = Food(food)
            else:
                all_foods[food].is_used()
        for allergen in allergens.split(", "):
            if allergen in all_allergens:
                all_allergens[allergen].food &= set(recipe_foods)
            else:
                all_allergens[allergen] = Allergen(allergen, recipe_foods)

    dangerous_ingredients = reduce(lambda a, b: a | b, [a.food for a in all_allergens.values()])
    print(sum(all_foods[food].amounts_used for food in all_foods if not food in dangerous_ingredients))





def solve_star2():
    all_foods = {}
    all_allergens = {}
    for line in read_file():
        recipe_foods, allergens = line[:-1].split(" (contains ")
        recipe_foods = recipe_foods.split(" ")
        for food in recipe_foods:
            if food not in all_foods:
                all_foods[food] = Food(food)
            else:
                all_foods[food].is_used()
        for allergen in allergens.split(", "):
            if allergen in all_allergens:
                all_allergens[allergen].food &= set(recipe_foods)
            else:
                all_allergens[allergen] = Allergen(allergen, recipe_foods)

    dangerous_ingredients = reduce(lambda a, b: a | b, [a.food for a in all_allergens.values()])

    while [allergen for allergen in all_allergens.values() if not allergen.found_origin()]:
        for allergen in all_allergens.values():
            source = allergen.check_origin()
            if source:
                for other in all_allergens.values():
                    if not other.found_origin():
                        other.remove(source)

    print(",".join([allergen.food for allergen in sorted(all_allergens.values(), key=lambda a : a.name)]))



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









