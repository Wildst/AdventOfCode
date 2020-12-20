#! /usr/bin/python
import sys, getopt
from math import prod

class Tile():
    def __init__(self, id, picture):
        self.id = id
        self.picture = picture
        self.neighbours = False

    def get_stripped_picture(self):
        return [line[1:-1] for line in self.picture[1:-1]]

    def show(self):
        for line in self.picture:
            print(line)
    def __str__(self):
        return "Tile " + str(self.id)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.id == other.id

    def get_edges(self):
        edges = []
        edges.append(self.picture[0])                              # North
        edges.append("".join(line[-1] for line in self.picture))   # East
        edges.append(self.picture[-1])                             # South
        edges.append("".join(line[0] for line in self.picture))    # West
        return edges

    def possible_neighbour(self, other_tile):
        if other_tile == self:
            return False
        for edge in self.get_edges():
            for other_edge in other_tile.get_edges():
                if edge == other_edge or edge == other_edge[::-1]:
                    return True
        return False

    def rotate(self):
        self.picture = rotate(self.picture)

    def flip(self):
        self.picture = flip(self.picture)

    def possible_neighbours(self, tiles):
        if not self.neighbours:
            self.neighbours = [tile.id for tile in tiles if self.possible_neighbour(tile)]
        return self.neighbours

    def get_neighbour_count(self, tiles):
        return len(self.possible_neighbours(tiles))

def flip(picture):
    return picture[::-1]

def rotate(picture):
    return ["".join([picture[j][i] for j in range(len(picture[0])-1, -1, -1)]) for i in range(len(picture))]

def solve_star1():
    cur_image = []
    cur_id = -1
    tiles = []
    for line in read_file():
        if "Tile" in line:
            cur_id = int(line[5:-1])
        elif line:
            cur_image.append(line)
        else:
            tiles.append(Tile(cur_id, cur_image))
            cur_id = -1
            cur_image = []
    tiles.append(Tile(cur_id, cur_image))
    print(prod([tile.id for tile in tiles if len(tile.possible_neighbours(tiles)) == 2]))

def solve_star2():
    cur_image = []
    cur_id = -1
    tiles = {}
    for line in read_file():
        if "Tile" in line:
            cur_id = int(line[5:-1])
        elif line:
            cur_image.append(line)
        else:
            tiles[cur_id] = Tile(cur_id, cur_image)
            cur_id = -1
            cur_image = []
    tiles[cur_id] = Tile(cur_id, cur_image)
    corners = [tile.id for tile in tiles.values() if len(tile.possible_neighbours(tiles.values())) == 2]


    col_tile = tiles[corners[0]]

    # Turn top left corner in the right direction
    edges = col_tile.get_edges()
    neighbouring_edges = [ edge for nb_id in col_tile.possible_neighbours(tiles.values) for edge in tiles[nb_id].get_edges()]

    while (edges[1] not in neighbouring_edges and edges[1][::-1] not in neighbouring_edges) or \
          (edges[2] not in neighbouring_edges and edges[2][::-1] not in neighbouring_edges):
        col_tile.rotate()
        edges = col_tile.get_edges()

    picture = []
    assembling_picture = True
    # Assemble picture
    while assembling_picture:
        assembling_row = True
        row_tile = col_tile
        row = [line for line in row_tile.get_stripped_picture()]

        # assemble next row
        while assembling_row:
            # Find next tile
            neighbours = row_tile.possible_neighbours(tiles.values)
            east_edge = row_tile.get_edges()[1]
            i = 0
            while east_edge not in tiles[neighbours[i]].get_edges() and \
                  east_edge[::-1] not in tiles[neighbours[i]].get_edges():
                i += 1
            next_tile = tiles[neighbours[i]]

            # rotate and/or flip tile
            while east_edge != next_tile.get_edges()[3] and east_edge[::-1] != next_tile.get_edges()[3]:
                next_tile.rotate()
            if east_edge != next_tile.get_edges()[3]:
                next_tile.flip()

            # add tile to row
            row = [a + b for (a, b) in zip(row, next_tile.get_stripped_picture())]

            # check if it was the last tile
            assembling_row = row_tile.get_neighbour_count(tiles) <= next_tile.get_neighbour_count(tiles)
            row_tile = next_tile

        # add row to picure
        for line in row:
            picture.append(line)

        # check if this was the last row
        neighbours = col_tile.possible_neighbours(tiles.values())
        south_edge = col_tile.get_edges()[2]
        neighbouring_edges = [ edge for nb_id in neighbours for edge in tiles[nb_id].get_edges()]

        # stop loop if necessary
        assembling_picture = south_edge in neighbouring_edges or south_edge[::-1] in neighbouring_edges

        # add first tile of next row
        if assembling_picture:
            # find next tile
            i = 0
            while south_edge not in tiles[neighbours[i]].get_edges() and \
                    south_edge[::-1] not in tiles[neighbours[i]].get_edges():
                i += 1
            col_tile = tiles[neighbours[i]]

            # rotate and/or flip tile
            while south_edge != col_tile.get_edges()[0] and south_edge[::-1] != col_tile.get_edges()[0]:
                col_tile.rotate()
            if south_edge != col_tile.get_edges()[0]:
                col_tile.rotate()
                col_tile.flip()
                col_tile.rotate()
                col_tile.rotate()
                col_tile.rotate()

    #####################
    # find sea monsters #
    #####################
    for i in range(4):
        check_for_monsters(picture)
        picture = rotate(picture)
    picture = flip(picture)
    for i in range(4):
        check_for_monsters(picture)
        picture = rotate(picture)

    picture = flip(picture)
    ################
    # get solution #
    ################
    print(sum([row.count("#") for row in picture]))

SEA_MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]
def check_for_monsters(picture):
    for start_row in range(len(picture)-len(SEA_MONSTER) + 1):
        for start_col in range(len(picture[0]) - len(SEA_MONSTER[0]) + 1):
            if is_monster(picture, start_row, start_col):
                place_monster(picture, start_row, start_col)

def is_monster(picture, start_row, start_col):
    for i, line in enumerate(SEA_MONSTER):
        for j, char in enumerate(line):
            if char == '#' and picture[start_row + i][start_col + j] == '.':
                return False
    return True

def place_monster(picture, start_row, start_col):
    for i, line in enumerate(SEA_MONSTER):
        for j, char in enumerate(line):
            if char == '#' and picture[start_row + i][start_col + j] == '#':
                row = picture[start_row + i]
                picture[start_row + i] = row[:start_col +j] + "O" + row[start_col +j + 1:]

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









